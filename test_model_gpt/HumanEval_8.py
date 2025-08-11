"""
Utility module for basic numeric operations.
"""

from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """Return a tuple of the sum and product of all integers in `numbers`.

    For an empty list, the sum is 0 and the product is 1.
    """
    assert all(isinstance(v, int) for v in numbers), "invalid inputs"
    total_sum = 0
    total_product = 1
    for value in numbers:
        total_sum += value
        total_product *= value
    return total_sum, total_product
