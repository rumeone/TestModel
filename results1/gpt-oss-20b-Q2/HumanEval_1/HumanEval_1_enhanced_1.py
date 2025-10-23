"""
Utility to split a string containing multiple balanced parenthesis groups
into a list of the individual groups.
"""

from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Split a string of balanced parenthesis groups into separate group strings.
    Groups are not nested within each other; only top‑level groups are returned.
    Spaces are ignored.
    Example:
        >>> separate_paren_groups('( ) (( )) (( )( ))')
        ['()', '(())', '(()())']
    """
    # Remove all whitespace to simplify parsing
    cleaned = "".join(ch for ch in paren_string if not ch.isspace())

    groups: List[str] = []
    current: List[str] = []
    depth = 0

    for ch in cleaned:
        if ch == "(":
            if depth == 0:          # start of a new top‑level group
                current = [ch]
            else:
                current.append(ch)
            depth += 1
        elif ch == ")":
            depth -= 1
            current.append(ch)
            if depth == 0:          # group closed
                groups.append("".join(current))
                current = []
        else:
            # ignore unexpected characters (should not occur)
            continue

    return groups