from typing import List


def separate_paren_groups(paren_string: str) -> List[str]:
    """
    Separate balanced parenthesis groups from a string.

    Parameters
    ----------
    paren_string : str
        A string that may contain multiple groups of nested parentheses.
        Groups are separated by whitespace or other characters but are not nested within each other.
        Spaces are ignored.

    Returns
    -------
    List[str]
        A list of the extracted groups, each including its outermost parentheses.

    Examples
    --------
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Remove all whitespace to simplify parsing
    cleaned = paren_string.replace(" ", "")
    groups: List[str] = []
    start = None
    depth = 0

    for idx, ch in enumerate(cleaned):
        if ch == "(":
            if depth == 0:
                start = idx
            depth += 1
        elif ch == ")":
            depth -= 1
            if depth == 0 and start is not None:
                groups.append(cleaned[start:idx + 1])
                start = None

    return groups