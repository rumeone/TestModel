from typing import List

# HumanEval/0
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than given threshold.
    """
    if not numbers:
        return False
    numbers_sorted = sorted(numbers)
    for i in range(1, len(numbers_sorted)):
        if numbers_sorted[i] - numbers_sorted[i-1] < threshold:
            return True
    return False

