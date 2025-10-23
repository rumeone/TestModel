"""
Utility module for simple list transformations.
"""

from typing import List


def rolling_max(numbers: List[int]) -> List[int]:
    """
    Return a list of rolling maximums for the input list of integers.
    The i-th element of the result is the maximum of numbers[:i+1].
    Example:
        >>> rolling_max([1, 2, 3, 2, 3, 4, 2])
        [1, 2, 3, 3, 3, 4, 4]
    """
    result: List[int] = []
    current_max: int | None = None  # keep track of the maximum seen so far

    for num in numbers:
        # update the running maximum
        if current_max is None or num > current_max:
            current_max = num
        # append the current maximum to the result
        result.append(current_max)

    return result