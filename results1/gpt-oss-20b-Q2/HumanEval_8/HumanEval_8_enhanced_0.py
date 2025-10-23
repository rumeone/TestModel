"""
Utility module for simple numeric operations.
"""

from typing import List, Tuple


def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """
    Return a tuple (total_sum, total_product) for the given list of integers.
    Empty list yields (0, 1).
    """
    total_sum = 0
    total_product = 1
    for n in numbers:  # iterate over each integer
        total_sum += n
        total_product *= n
    return total_sum, total_product