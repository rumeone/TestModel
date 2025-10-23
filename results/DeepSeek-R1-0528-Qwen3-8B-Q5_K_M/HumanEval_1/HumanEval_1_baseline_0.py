from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """ Input to this function is a string containing multiple groups of nested parentheses. Your goal is to
    separate those group into separate strings and return the list of those.
    Separate groups are balanced (each open brace is properly closed) and not nested within each other
    Ignore any spaces in the input string.
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    paren_string = paren_string.replace(" ", "")
    groups = []
    start = 0
    i = 0
    n = len(paren_string)
    while i < n:
        if paren_string[i] == '(':
            start = i
            count = 1
            i += 1
            while i < n and count != 0:
                if paren_string[i] == '(':
                    count += 1
                elif paren_string[i] == ')':
                    count -= 1
                i += 1
            if count == 0:
                groups.append(paren_string[start:i])
                i -= 1  # because the while loop increments i, so we need to step back to the next character
        i += 1
    return groups