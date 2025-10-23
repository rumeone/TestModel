from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """Input is a string of multiple groups of nested parentheses separated by spaces.
    Output the deepest level of nesting for each group.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    groups = paren_string.split()
    result = []
    for group in groups:
        current_level = 0
        max_level = 0
        for char in group:
            if char == '(':
                current_level += 1
                if current_level > max_level:
                    max_level = current_level
            elif char == ')':
                current_level -= 1
        result.append(max_level)
    return result