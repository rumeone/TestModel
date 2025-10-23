import matplotlib.pyplot as plt
import numpy as np

# ==========================
# ДАННЫЕ ДЛЯ DEEPSEEK
# ==========================
deepseek_no_rules = [
    7.14, 7.83, 0.00, 6.25, 7.50,
    6.25, 7.50, 0.00, 6.67, 6.92,
    7.00, 6.36, 7.27, 5.00, 3.33
]

deepseek_with_rules = [
    7.14, 8.95, 0.00, 7.50, 6.67,
    8.00, 7.65, 3.33, 5.71, 6.67,
    6.67, 6.43, 8.46, 5.00, 6.67
]

deepseek_few_shot = [
    7.78, 8.67, 0.00, 6.25, 7.78,
    7.78, 8.12, 3.33, 7.14, 6.92,
    7.00, 5.00, 8.18, 5.00, 3.33
]

# ==========================
# ДАННЫЕ ДЛЯ GPT
# ==========================
gpt_no_rules = [
    8.00, 8.33, 6.67, 6.25, 7.78,
    7.00, 7.78, 3.33, 6.25, 6.67,
    7.86, 5.00, 6.00, 6.00, 6.25
]

gpt_with_rules = [
    8.89, 9.44, 6.67, 8.75, 8.89,
    9.00, 8.89, 6.67, 8.75, 8.89,
    9.00, 8.89, 9.17, 8.89, 8.33
]

gpt_few_shot = [
    7.00, 7.27, 8.82, 5.00, 7.14,
    8.00, 6.67, 3.33, 7.50, 7.78,
    8.33, 5.00, 8.18, 4.00, 5.00
]

# ==========================
# НАСТРОЙКИ ДЛЯ ГРАФИКОВ
# ==========================
x = np.arange(15)  # HumanEval_0 ... HumanEval_14
width = 0.25  # Ширина столбцов

# ==========================
# ГРАФИК 1 — DEEPSEEK (СТОЛБЧАТАЯ ДИАГРАММА)
# ==========================
plt.figure(figsize=(15, 8))

# Создаем позиции для столбцов
x1 = x - width
x2 = x
x3 = x + width

# Рисуем столбцы
plt.bar(x1, deepseek_no_rules, width, label='No Rules', alpha=0.8)
plt.bar(x2, deepseek_with_rules, width, label='With Rules', alpha=0.8)
plt.bar(x3, deepseek_few_shot, width, label='Few Shot', alpha=0.8)

plt.title('DeepSeek-R1-0528-Qwen3-8B-Q5_K_M — HumanEval Scores', fontsize=14, fontweight='bold')
plt.xlabel('HumanEval Task', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.xticks(x, [f'Task {i}' for i in range(15)])
plt.ylim(0, 10)
plt.grid(True, linestyle='--', alpha=0.3, axis='y')
plt.legend()
plt.tight_layout()
plt.show()

# ==========================
# ГРАФИК 2 — GPT (СТОЛБЧАТАЯ ДИАГРАММА)
# ==========================
plt.figure(figsize=(15, 8))

# Рисуем столбцы
plt.bar(x1, gpt_no_rules, width, label='No Rules', alpha=0.8)
plt.bar(x2, gpt_with_rules, width, label='With Rules', alpha=0.8)
plt.bar(x3, gpt_few_shot, width, label='Few Shot', alpha=0.8)

plt.title('gpt-oss-20b-Q2 — HumanEval Scores', fontsize=14, fontweight='bold')
plt.xlabel('HumanEval Task', fontsize=12)
plt.ylabel('Score', fontsize=12)
plt.xticks(x, [f'Task {i}' for i in range(15)])
plt.ylim(0, 10)
plt.grid(True, linestyle='--', alpha=0.3, axis='y')
plt.legend()
plt.tight_layout()
plt.show()

# ==========================
# ГРАФИК 3 — СРАВНЕНИЕ СРЕДНИХ ЗНАЧЕНИЙ
# ==========================
models = ['DeepSeek No Rules', 'DeepSeek With Rules', 'DeepSeek Few Shot', 
          'GPT No Rules', 'GPT With Rules', 'GPT Few Shot']

averages = [
    sum(deepseek_no_rules)/15,
    sum(deepseek_with_rules)/15,
    sum(deepseek_few_shot)/15,
    sum(gpt_no_rules)/15,
    sum(gpt_with_rules)/15,
    sum(gpt_few_shot)/15
]

colors = ['lightblue', 'lightgreen', 'lightcoral', 
          'blue', 'green', 'red']

plt.figure(figsize=(12, 6))
bars = plt.bar(models, averages, color=colors, alpha=0.8)

# Добавляем значения на столбцы
for bar, value in zip(bars, averages):
    plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.05, 
             f'{value:.2f}', ha='center', va='bottom', fontweight='bold')

plt.title('Average Scores Comparison', fontsize=14, fontweight='bold')
plt.ylabel('Average Score', fontsize=12)
plt.ylim(0, 10)
plt.grid(True, linestyle='--', alpha=0.3, axis='y')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()