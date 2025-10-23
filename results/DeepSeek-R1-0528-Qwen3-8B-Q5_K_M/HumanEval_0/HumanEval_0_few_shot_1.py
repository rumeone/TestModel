
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if any two numbers in the list are closer than the threshold.
    Args:
        numbers: List of numbers to check.
        threshold: The minimum distance to consider as not close.
    Returns:
        bool: True if any two numbers are closer than threshold, False otherwise.
    """
    if len(numbers) < 2:
        return False
    numbers.sort()
    for i in range(len(numbers) - 1):
        if numbers[i+1] - numbers[i] < threshold:
            return True
    return False