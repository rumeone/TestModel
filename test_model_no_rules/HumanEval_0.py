# HumanEval/0
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    if not numbers:
        return False
    numbers_sorted = sorted(numbers)
    for i in range(len(numbers_sorted) - 1):
        if numbers_sorted[i+1] - numbers_sorted[i] < threshold:
            return True
    return False

