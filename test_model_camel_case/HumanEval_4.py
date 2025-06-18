# HumanEval/4
from typing import List


def mean_absolute_deviation(numbers: List[float]) -> float:
    """Calculate the Mean Absolute Deviation of a list of numbers.
    
    Args:
        numbers: List of float values representing the dataset.
        
    Returns:
        float: The average absolute difference between each number and the mean.
        
    Example:
        >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
        1.0
    """
    assert all(isinstance(x, float) for x in numbers), "invalid inputs"
    assert numbers != [], "invalid inputs"
    
    total = 0.0
    for num in numbers:
        total += abs(num - sum(numbers) / len(numbers))
    
    return total / len(numbers)
