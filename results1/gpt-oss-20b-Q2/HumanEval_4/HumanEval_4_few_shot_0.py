from typing import List

def mean_absolute_deviation(numbers: List[float]) -> float:
    """Return the mean absolute deviation of *numbers* around their mean.

    The mean absolute deviation (MAD) is the average of the absolute
    differences between each element and the dataset mean:

        MAD = (1 / n) * Σ |xᵢ – mean|

    Parameters
    ----------
    numbers : List[float]
        A non‑empty list of numeric values.

    Returns
    -------
    float
        The mean absolute deviation.

    Raises
    ------
    ValueError
        If *numbers* is empty.

    Examples
    --------
    >>> mean_absolute_deviation([1.0, 2.0, 3.0, 4.0])
    1.0
    """
    if not numbers:
        raise ValueError("input list must contain at least one element")

    mean_val = sum(numbers) / len(numbers)
    total_abs_diff = sum(abs(x - mean_val) for x in numbers)
    return total_abs_diff / len(numbers)