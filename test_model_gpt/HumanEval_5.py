"""
Utility module for list manipulation.
"""

from typing import List


def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number `delimeter` between every two consecutive elements of input list `numbers`.

    >>> intersperse([], 4)
    []
    >>> intersperse([1, 2, 3], 4)
    [1, 4, 2, 4, 3]
    """
    assert all(isinstance(v, int) for v in numbers), "invalid inputs"
    assert isinstance(delimeter, int), "invalid inputs"

    if not numbers:
        return []

    result = [numbers[0]]
    for value in numbers[1:]:
        result.append(delimeter)
        result.append(value)
    return result
