"""
Module containing a function to check if a sequence of bank operations ever drops the balance below zero.
"""

from typing import List


def below_zero(operations: List[int]) -> bool:
    """Return True if the running balance ever falls below zero, otherwise False."""
    assert type(operations) == list, "invalid inputs"
    assert all(isinstance(v, int) for v in operations), "invalid inputs"
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
