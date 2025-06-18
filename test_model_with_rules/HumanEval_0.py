# HumanEval/0
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if any two numbers in the list are closer than the threshold.

    Args:
        numbers: List of numbers to check.
        threshold: Minimum distance required between any two numbers.

    Returns:
        bool: True if any two numbers are closer than threshold, False otherwise.
    """
    if not numbers:
        return False
    numbers.sort()
    for i in range(1, len(numbers)):
        if numbers[i] - numbers[i-1] < threshold:
            return True
    return False
