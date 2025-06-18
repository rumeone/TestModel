# HumanEval/9
from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """Generate a list of rolling maximum integers from the input list.

    Args:
        numbers: List of integers.

    Returns:
        List of integers where each element is the maximum value seen so far in the sequence.

    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    if not numbers:
        return []
    current_max = numbers[0]
    result = [current_max]
    for num in numbers[1:]:
        if num > current_max:
            current_max = num
            result.append(current_max)
        else:
            result.append(current_max)
    return result
