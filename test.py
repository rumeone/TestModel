import os
import json
import re
from llama_cpp import Llama

MODEL_PATH = r"F:\LLM\DeepSeek-R1-0528-Qwen3-8B-Q5_K_M.gguf"
DATASET_PATH = "HumanEvalPlus-Mini.jsonl"
OUT_DIR = "test_model"     
LIMIT = 15  

os.makedirs(OUT_DIR, exist_ok=True)

SYSTEM_INSTRUCTIONS = """
You are an expert Python programmer. The user will provide a function specification.
Generate a complete implementation of the function including:
All code must strictly use snake_case for all variables and function names.
1. All necessary imports (if needed)
2. The function signature from the specification
3. Names must be meaningful and beginner-friendly.
4. Adhere to PEP8 (4-space indent, max line length 79, spaces around operators).
5. Avoid nesting deeper than 2 levels (if/for/while).
6. Do NOT include any reasoning, thought process, or step-by-step comments in the code.
7. Include a concise module-level docstring and a concise function docstring only.
Format your response as:

```python
# Imports (if needed)
def functionName(...):
    \"\"\"Docstring\"\"\"
"""

def load_tasks(path, limit=None):
    with open(path, encoding="utf-8") as f:
        lines = f.readlines()[:limit] if limit else f.readlines()
    return [json.loads(line) for line in lines]

def extract_code(response: str) -> str:
    m = re.search(r"```python\n(.*?)\n```", response, re.DOTALL)
    if m:
        return m.group(1).strip()
    m2 = re.search(r"(def\s+\w+\s*\(.*)", response, re.DOTALL)
    if m2:
        return m2.group(1).strip()
    return response.strip()

def generate_complete_function(llama, prompt: str, contract: str) -> str:
    full_prompt = (
        "<|im_start|>system\n"
        f"{SYSTEM_INSTRUCTIONS.strip()}\n"
        "<|im_end|>\n"
        "<|im_start|>user\n"
        "Function specification:\n"
        f"{prompt}\n\n"
        "Contract conditions:\n"
        f"{contract}\n\n"
        "Generate the complete function implementation in Python.\n"
        "<|im_end|>\n"
        "<|im_start|>assistant\n"
    )

    resp = llama(
        prompt=full_prompt,
        max_tokens=1024,
        temperature=0.0,
        top_p=0.9,
        stop=["<|im_end|>", "```end"],
        echo=False
    )
    return resp["choices"][0]["text"]

def save_solution(task_id: str, code: str):
    filename = task_id.replace("/", "_") + ".py"
    path = os.path.join(OUT_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(f"# {task_id}\n")
        f.write(code.strip() + "\n")
    return path

def main():
    llama = Llama(
        model_path=MODEL_PATH,
        n_ctx=16384,
        n_gpu_layers=60,
        n_threads=8,
        use_mlock=True,
        verbose=False
    )

    tasks = load_tasks(DATASET_PATH, LIMIT)
    for task in tasks:
        tid = task["task_id"]
        prompt = task["prompt"].rstrip() + "\n"
        contract = task["contract"].rstrip() + "\n"

        response = generate_complete_function(llama, prompt, contract)
        code = extract_code(response)

        out_path = save_solution(tid, code)
        print(f"✅ {tid} → saved to {out_path}")

if __name__ == "__main__":
    main()
