from typing import List

# HumanEval/4
def mean_absolute_deviation(numbers: List[float]) -> float:
    """Calculate the Mean Absolute Deviation of a list of numbers.
    
    Args:
        numbers: List of float numbers.
        
    Returns:
        float: The MAD value.
    """
    if not numbers:
        raise AssertionError("invalid inputs")
    assert all(isinstance(x, float) for x in numbers), "invalid inputs"
    mean = sum(numbers) / len(numbers)
    deviations = [abs(x - mean) for x in numbers]
    mad = sum(deviations) / len(numbers)
    return mad
