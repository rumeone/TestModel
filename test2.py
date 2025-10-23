#!/usr/bin/env python3
# coding: utf-8

import os
import json
import re
import time
import shutil
import subprocess
import tempfile
from datetime import datetime
from pathlib import Path
from typing import Dict, Any, List

from llama_cpp import Llama

# ----------------------------
# ========== CONFIG ==========
# ----------------------------
MODEL_PATH = r"F:\LLM\DeepSeek-R1-0528-Qwen3-8B-Q5_K_M.gguf"   
DATASET_PATH = "HumanEvalPlus-Mini.jsonl"     
OUT_ROOT = "results"                          
LIMIT = 15                                    
SAMPLES_PER_PROMPT = 2                         
BASE_SEED = 42                       

GEN_PARAMS = {
    "temperature": 0.2,
    "top_p": 0.9,
    "max_tokens": 1024,
}
MODELS = [
    {"name": "DeepSeek-R1-0528-Qwen3-8B-Q5_K_M.gguf", "path": MODEL_PATH},
]


SYSTEM_INSTRUCTIONS = """
You are an expert Python programmer. 
STRICT RULES:
- Do NOT include any reasoning, thoughts, or explanations.
- NEVER output <think> or any text outside a code block.
"""

PROMPTS = {
    "baseline": """You are a Python programmer. Implement the function specified below. Return only valid Python code (no explanations).
{task_prompt}
""",
    "enhanced": """You are an expert Python programmer. Generate a complete implementation of the function specified below.
Requirements:
- Use PEP8 formatting (4-space indent, max line length 79).
- Use meaningful snake_case names for functions and variables.
- Provide a concise module-level docstring and a concise function docstring.
- Avoid nesting deeper than 2 levels.
- Add brief inline comments for key lines only.
- Include all necessary imports.
Return only a single ```python``` code block with the implementation (no surrounding text).
{task_prompt}
""",
    "few_shot": """Example:
# Input: brief spec
# Output:
def example_func(x):
    \"\"\"Example docstring\"\"\"
    return x * 2

Now implement the function below following the example's style (concise docstring, clear naming).
{task_prompt}
"""
}

def load_tasks(path: str, limit: int = None) -> List[Dict[str, Any]]:
    """Load tasks from a JSONL file. Each line - JSON object with fields task_id, prompt, test/contract."""
    tasks = []
    with open(path, "r", encoding="utf-8") as f:
        for idx, line in enumerate(f):
            if limit and idx >= limit:
                break
            line = line.strip()
            if not line:
                continue
            try:
                obj = json.loads(line)
            except Exception as e:
                print(f"Skipping invalid JSON line {idx}: {e}")
                continue
            tasks.append(obj)
    return tasks


def extract_code(response: str) -> str:
    """
    Extract python code from a model response.
    Prefer ```python``` blocks, otherwise try to capture first def ...: block, else return whole text.
    """
    if not response:
        return ""

    # Удаляем блоки размышлений <think>...</think>
    response = re.sub(r"<think>.*?</think>", "", response, flags=re.DOTALL)

    # Normalize CRLF
    response = response.replace("\r\n", "\n")

    # 1) code block ```python ... ```
    m = re.search(r"```python\s*\n(.*?)\n```", response, re.DOTALL)
    if m:
        return m.group(1).strip()

    # 2) any ``` ... ``` block
    m2 = re.search(r"```\s*\n(.*?)\n```", response, re.DOTALL)
    if m2:
        return m2.group(1).strip()

    # 3) first def ... (grab until next top-level blank line or end)
    m3 = re.search(r"(def\s+\w+\s*\(.*\):[\s\S]*)", response)
    if m3:
        txt = m3.group(1).strip()
        return txt

    return response.strip()


def run_experiment_for_model(model_spec: Dict[str, str], tasks: List[Dict[str, Any]]):
    model_name = model_spec["name"]
    model_path = model_spec["path"]
    out_dir_model = Path(OUT_ROOT) / model_name
    out_dir_model.mkdir(parents=True, exist_ok=True)

    print(f"[{datetime.now()}] Initializing model {model_name} from {model_path}")
    llm = Llama(
        model_path=model_path,
        n_ctx=8192,
        n_gpu_layers=60,
        n_threads=16,
        verbose=False
    )

    for task in tasks:
        task_id = task.get("task_id", f"task_unknown_{int(time.time())}")
        task_prompt = task.get("prompt", "")

        task_folder = out_dir_model / task_id.replace("/", "_")
        task_folder.mkdir(parents=True, exist_ok=True)

        for prompt_name, template in PROMPTS.items():
            full_prompt = template.format(task_prompt=task_prompt)

            for sample_idx in range(SAMPLES_PER_PROMPT):
                seed = BASE_SEED + sample_idx
                gen_params = dict(GEN_PARAMS)
                gen_params["seed"] = seed

                prompt_text = (
                    "<|im_start|>system\n"
                    f"{SYSTEM_INSTRUCTIONS.strip()}\n"
                    "<|im_end|>\n"
                    "<|im_start|>user\n"
                    f"{full_prompt}\n"
                    "<|im_end|>\n"
                    "<|im_start|>assistant\n"
                )

                try:
                    start_ts = time.time()
                    resp = llm(
                        prompt=prompt_text,
                        max_tokens=gen_params["max_tokens"],
                        temperature=gen_params["temperature"],
                        top_p=gen_params["top_p"],
                        stop=["<|im_end|>"],   # чтобы гарантированно не было хвостов
                        echo=False
                    )
                    latency = time.time() - start_ts
                except Exception as e:
                    print(f"[ERR] model generation failed for {task_id} {prompt_name} sample{sample_idx}: {e}")
                    resp = {"choices": [{"text": ""}]}
                    latency = None

                try:
                    raw_text = resp["choices"][0]["text"]
                except Exception:
                    raw_text = str(resp)

                extracted = extract_code(raw_text)

                file_name = f"{task_id.replace('/', '_')}_{prompt_name}_{sample_idx}.py"
                out_code = task_folder / file_name

                with open(out_code, "w", encoding="utf-8") as f:
                    f.write(extracted)

                result = {
                    "timestamp": datetime.utcnow().isoformat(),
                    "task_id": task_id,
                    "prompt_name": prompt_name,
                    "seed": seed,
                    "sample_idx": sample_idx,
                    "generation_params": gen_params,
                    "latency_s": latency,
                    "extracted_code": extracted,
                    "code_file": str(out_code),
                }
def main():
    tasks = load_tasks(DATASET_PATH, limit=LIMIT)
    if not tasks:
        print("No tasks loaded. Check DATASET_PATH.")
        return

    for model_spec in MODELS:
        run_experiment_for_model(model_spec, tasks)


if __name__ == "__main__":
    main()
