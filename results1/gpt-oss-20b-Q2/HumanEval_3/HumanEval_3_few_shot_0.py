from typing import List


def below_zero(operations: List[int]) -> bool:
    """Return True if the account balance ever falls below zero during the sequence of operations.

    The account starts with a zero balance. Each integer in *operations* represents a deposit (positive)
    or withdrawal (negative). The function returns True as soon as the cumulative sum becomes negative,
    otherwise it returns False.

    Examples:
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