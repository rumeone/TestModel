import os
import subprocess
import re

root_dir = 'results/DeepSeek-R1-0528-Qwen3-8B-Q5_K_M'

output_file = 'pylint_results_full_deepseek.txt'


score_pattern = re.compile(r'rated at ([-+]?\d*\.\d+|\d+)/10')


with open(output_file, 'w', encoding='utf-8') as result_file:

    for folder_name in os.listdir(root_dir):
        folder_path = os.path.join(root_dir, folder_name)
        
        if os.path.isdir(folder_path) and folder_name.startswith('HumanEval_'):
            for file_name in os.listdir(folder_path):
                if file_name.endswith('.py'):
                    file_path = os.path.join(folder_path, file_name)
                    full_file_path = f"{root_dir}/{folder_name}/{file_name}"
                    
                    print(f"Processing: {file_path}")
                    

                    result_file.write(f"File: {full_file_path}\n")
                    result_file.write("=" * 50 + "\n")
                    
                    try:
                        result = subprocess.run([
                            'python', '-m', 'pylint',
                            '--output-format=text',
                            '--score=yes',
                            '--disable=C0103',
                            file_path
                        ], capture_output=True, text=True, timeout=30, encoding='utf-8')
                        
     
                        result_file.write(result.stdout)
                        
   
                        if result.stderr:
                            result_file.write("\nSTDERR:\n")
                            result_file.write(result.stderr)
                            
                        result_file.write("\n" + "=" * 50 + "\n\n")
                        
                    except subprocess.TimeoutExpired:
                        result_file.write(f"Timeout after 30 seconds\n")
                        result_file.write("=" * 50 + "\n\n")
                    except Exception as e:
                        result_file.write(f"Exception: {str(e)}\n")
                        result_file.write("=" * 50 + "\n\n")

print(f"Results saved to {output_file}")