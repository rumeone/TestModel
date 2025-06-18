# HumanEval/4
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """Calculate the Mean Absolute Deviation (MAD) for a list of numbers.
    The MAD is the average absolute difference between each element and the mean.
    """
    assert all(isinstance(x, float) for x in numbers), "invalid inputs"
    assert numbers != [], "invalid inputs"
    n = len(numbers)
    mean = sum(numbers) / n
    deviations = [abs(x - mean) for x in numbers]
    mad = sum(deviations) / n
    return mad
