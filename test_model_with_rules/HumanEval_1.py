# HumanEval/1
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """Separates balanced groups of nested parentheses from the input string and returns them as a list."""
    paren_string = paren_string.replace(" ", "")
    groups = []
    start = 0
    current_group = ''
    for i, char in enumerate(paren_string):
        if char == '(':
            if current_group and not current_group.endswith(')'):
                groups.append(current_group)
                current_group = ''
            start = i
        elif char == ')':
            if i - start == 1:
                groups.append(current_group)
                current_group = ''
            else:
                current_group += char
    if current_group:
        groups.append(current_group)
    return groups
