import numpy as np
from scipy import stats

# =======================
# ДАННЫЕ
# =======================
deepseek_baseline = [
    7.14, 7.83, 0.00, 6.25, 7.50,
    6.25, 7.50, 0.00, 6.67, 6.92,
    7.00, 6.36, 7.27, 5.00, 3.33
]

deepseek_enhanced = [
    7.14, 8.95, 0.00, 7.50, 6.67,
    8.00, 7.65, 3.33, 5.71, 6.67,
    6.67, 6.43, 8.46, 5.00, 6.67
]

gpt_baseline = [
    8.00, 8.33, 6.67, 6.25, 7.78,
    7.00, 7.78, 3.33, 6.25, 6.67,
    7.86, 5.00, 6.00, 6.00, 6.25
]

gpt_enhanced = [
    8.89, 9.44, 6.67, 8.75, 8.89,
    9.00, 8.89, 6.67, 8.75, 8.89,
    9.00, 8.89, 9.17, 8.89, 8.33
]

# =======================
# ФУНКЦИЯ ДЛЯ Т-ТЕСТА
# =======================
def run_ttest(data1, data2, name):
    t_stat, p_val = stats.ttest_rel(data1, data2)
    print(f"{name} — t = {t_stat:.2f}, p = {p_val:.5f}")

# =======================
# ЗАПУСК ТЕСТОВ
# =======================
run_ttest(deepseek_baseline, deepseek_enhanced, "DeepSeek (Baseline vs Enhanced)")
run_ttest(gpt_baseline, gpt_enhanced, "GPT (Baseline vs Enhanced)")
