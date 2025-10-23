from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """Separate groups of nested parentheses from the input string into a list of balanced strings.
    Ignore spaces in the input string.
    """
    paren_string = paren_string.replace(' ', '')
    groups = []
    current_group = []
    depth = 0
    for char in paren_string:
        if char == '(':
            depth += 1
            current_group.append(char)
        elif char == ')':
            depth -= 1
            current_group.append(char)
            if depth == 0:
                groups.append(''.join(current_group))
                current_group = []
    if current_group:
        groups.append(''.join(current_group))
    return groups