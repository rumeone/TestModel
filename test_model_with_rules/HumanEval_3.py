# HumanEval/3
from typing import List

def below_zero(operations: List[int]) -> bool:
    """Detect if at any point the balance of account falls below zero during a series of operations.

    Args:
        operations: List of integers representing deposits (positive) and withdrawals (negative).

    Returns:
        bool: True if balance ever goes below zero, otherwise False.
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
