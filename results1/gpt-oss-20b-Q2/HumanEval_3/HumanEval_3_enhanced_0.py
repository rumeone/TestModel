"""
Utility to check if a sequence of bank operations ever drops the balance below zero.
"""

from typing import List


def below_zero(operations: List[int]) -> bool:
    """
    Return True if the cumulative balance ever becomes negative, otherwise False.

    Parameters
    ----------
    operations : List[int]
        A list of integers representing deposits (positive) and withdrawals (negative).

    Returns
    -------
    bool
        True if the balance falls below zero at any point, otherwise False.

    Examples
    --------
    >>> below_zero([1, 2, 3])
    False
    >>> below_zero([1, 2, -4, 5])
    True
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False