from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Separate groups of nested parentheses into balanced strings without spaces.
    Args:
        paren_string: Input string containing multiple groups of parentheses.
    Returns:
        List of balanced parentheses strings.
    """
    paren_string = paren_string.replace(' ', '')
    groups = []
    start = 0
    balance = 0
    for i, char in enumerate(paren_string):
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance == 0:
            groups.append(paren_string[start:i+1])
            start = i + 1
    return groups