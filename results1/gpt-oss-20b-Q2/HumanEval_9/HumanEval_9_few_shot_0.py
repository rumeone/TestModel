from typing import List

def rolling_max(numbers: List[int]) -> List[int]:
    """Return a list of rolling maximums for the given sequence of integers.

    For each position i, the i-th element of the result is the maximum of numbers[0:i+1].

    Example:
    >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
    [1, 2, 3, 3, 3, 4, 4]
    """
    result: List[int] = []
    current_max: int | None = None
    for n in numbers:
        if current_max is None or n > current_max:
            current_max = n
        result.append(current_max)
    return result