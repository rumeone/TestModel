"""
Module: parse_nested_parens
Provides a single function to compute the maximum depth of nested parentheses
in each group of a space‑separated string.
"""

from typing import List


def parse_nested_parens(paren_string: str) -> List[int]:
    """
    Parse a string containing groups of parentheses separated by spaces.
    For each group, return the deepest level of nested parentheses.
    Example:
        >>> parse_nested_parens('(()()) ((())) () ((())()())')
        [2, 3, 1, 3]
    """
    if not paren_string:
        return []

    groups = paren_string.split()
    depths: List[int] = []

    for group in groups:
        current_depth = 0
        max_depth = 0
        for ch in group:
            if ch == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif ch == ')':
                current_depth -= 1
        depths.append(max_depth)

    return depths