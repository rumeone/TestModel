# separate_paren_groups.py
"""
Separate balanced parenthesis groups from a string.
"""

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Return a list of balanced parenthesis groups from `paren_string`.

    The input string may contain spaces; they are ignored.  Each group is a
    contiguous sequence of parentheses that is balanced and not nested
    inside another group.  The function returns the groups in the order
    they appear in the input string.

    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove spaces to simplify processing
    cleaned = paren_string.replace(" ", "")
    result: List[str] = []
    current: List[str] = []
    depth = 0
    for ch in cleaned:
        if ch == "(":
            if depth == 0:
                current = []
            current.append(ch)
            depth += 1
        elif ch == ")":
            current.append(ch)
            depth -= 1
            if depth == 0:
                result.append("".join(current))
    return result
