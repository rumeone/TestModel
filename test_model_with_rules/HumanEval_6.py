# HumanEval/6
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """Given a string of multiple groups of nested parentheses separated by spaces, 
    returns a list of integers representing the deepest nesting level for each group.
    """
    groups = paren_string.split()
    result = []
    for group in groups:
        current_level = 0
        max_level = 0
        for char in group:
            if char == '(':
                current_level += 1
            elif char == ')':
                current_level -= 1
            else:
                # This else should not happen because groups are separated by spaces and split removes spaces
                current_level = 0
            if current_level > max_level:
                max_level = current_level
        result.append(max_level)
    return result
