from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Input to this function is a string containing multiple groups of nested parentheses.
    Your goal is to separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other.
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove all whitespace characters
    s = ''.join(paren_string.split())
    groups: List[str] = []
    if not s:
        return groups

    start = 0
    counter = 0
    for i, ch in enumerate(s):
        if ch == '(':
            if counter == 0:
                start = i
            counter += 1
        elif ch == ')':
            counter -= 1
            if counter == 0:
                groups.append(s[start:i+1])
    return groups