
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """Calculate Mean Absolute Deviation around the mean of the dataset.
    MAD = average | x - x_mean |
    Args:
        numbers: List of numbers for which to calculate MAD.
    Returns:
        The mean absolute deviation as a float.
    """
    n = len(numbers)
    if n == 0:
        return 0.0
    mean = sum(numbers) / n
    differences = [abs(x - mean) for x in numbers]
    mad = sum(differences) / n
    return mad