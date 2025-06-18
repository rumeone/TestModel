# HumanEval/9
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """Generate a list of rolling maximum integers from the input list."""
    if not numbers:
        return []
    result = []
    current_max = numbers[0]
    for num in numbers:
        if num > current_max:
            current_max = num
            result.append(current_max)
        else:
            result.append(current_max)
    return result
