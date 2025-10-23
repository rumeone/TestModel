from typing import List

def below_zero(operations: List[int]) -> bool:
    """Detects if at any point the balance falls below zero during a series of operations starting from zero."""
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False