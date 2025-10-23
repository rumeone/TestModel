
from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Check if any two numbers in the list are closer than the given threshold.

    Args:
        numbers: List of numbers to check.
        threshold: The minimum distance required between any two numbers.

    Returns:
        bool: True if any two numbers are closer than the threshold, False otherwise.

    Examples:
        >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
        False
        >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
        True
    """
    sorted_nums = sorted(numbers)
    for i in range(len(sorted_nums) - 1):
        if sorted_nums[i+1] - sorted_nums[i] < threshold:
            return True
    return False