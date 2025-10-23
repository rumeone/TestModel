from typing import List


def below_zero(operations: List[int]) -> bool:
    """Detect if at any point the balance of account falls below zero during a series of operations.
    The account starts with zero balance.
    Args:
        operations: List of integers representing deposit and withdrawal operations.
    Returns:
        bool: True if balance falls below zero at any point, False otherwise.
    """
    balance = 0
    for op in operations:
        balance += op
        if balance < 0:
            return True
    return False