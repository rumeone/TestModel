
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """Calculate Mean Absolute Deviation around the mean of the dataset.
    
    Mean Absolute Deviation is the average absolute difference between each
    element and the mean.
    
    Args:
        numbers: List of numbers for which to calculate MAD.
        
    Returns:
        float: The mean absolute deviation.
        
    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    if not numbers:
        return 0.0
        
    n = len(numbers)
    mean = sum(numbers) / n
    deviations = [abs(x - mean) for x in numbers]
    mad = sum(deviations) / n
    return mad