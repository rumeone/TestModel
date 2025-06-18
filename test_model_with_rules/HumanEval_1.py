# HumanEval/1
from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Separates balanced groups of nested parentheses from the input string, ignoring spaces.
    Each group is a string of parentheses without any spaces and is non-nested with other groups.
    """
    paren_string = paren_string.replace(" ", "")
    groups = []
    start = 0
    current_group = ""
    for i, char in enumerate(paren_string):
        if char == '(':
            if current_group:
                groups.append(current_group)
                current_group = ""
            start = i
        elif char == ')':
            if not current_group:
                raise ValueError("Invalid input: unmatched closing parenthesis")
            current_group += char
            if current_group[-1] == ')':
                if current_group.count('(') == current_group.count(')'):
                    groups.append(current_group)
                    current_group = ""
    if current_group:
        groups.append(current_group)
    return groups
