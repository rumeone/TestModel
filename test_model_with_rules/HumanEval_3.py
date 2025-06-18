from typing import List

# HumanEval/3
def below_zero(operations: List[int]) -> bool:
    """Detect if the account balance falls below zero at any point during the operations."""
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False
