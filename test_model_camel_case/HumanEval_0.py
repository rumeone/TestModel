# HumanEval/0
from typing import List


def hasCloseElements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    """
    if not isinstance(threshold, float) or threshold <= 0:
        raise ValueError("invalid inputs")
    if not isinstance(numbers, list):
        raise TypeError("invalid inputs")
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if abs(numbers[i] - numbers[j]) < threshold:
                return True
    return False
