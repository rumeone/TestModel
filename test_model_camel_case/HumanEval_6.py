# HumanEval/6
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """Given a string of multiple groups of nested parentheses separated by spaces, 
    returns a list of integers representing the deepest nesting level for each group.
    
    Args:
        paren_string: A string containing groups of parentheses separated by spaces.
        
    Returns:
        A list of integers where each integer is the maximum nesting depth of a group.
    """
    groups = paren_string.split()
    result = []
    for group in groups:
        current_depth = 0
        max_depth = 0
        for char in group:
            if char == '(':
                current_depth += 1
            elif char == ')':
                current_depth -= 1
            else:
                continue
            if current_depth > max_depth:
                max_depth = current_depth
        result.append(max_depth)
    return result
