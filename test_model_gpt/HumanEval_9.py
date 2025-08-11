"""
Module providing a rolling maximum calculation for a list of integers.
"""

from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """Return a list of rolling maximums for the input list of integers.

    The i-th element of the result is the maximum of numbers[0:i+1].
    """
    assert isinstance(numbers, list), "invalid inputs"
    assert all(isinstance(v, int) for v in numbers), "invalid inputs"

    result: List[int] = []
    current_max: int | None = None
    for value in numbers:
        if current_max is None or value > current_max:
            current_max = value
        result.append(current_max)
    return result
