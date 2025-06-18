# HumanEval/3
from typing import List

def belowZero(operations: List[int]) -> bool:
    """Detect if at any point the balance falls below zero during a series of operations."""
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
