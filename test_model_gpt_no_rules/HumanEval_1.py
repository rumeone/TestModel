def separate_paren_groups(paren_string: str):
    """Separate balanced parenthesis groups from a string.

    Parameters
    ----------
    paren_string : str
        String containing multiple groups of nested parentheses. The string may contain spaces which are ignored.

    Returns
    -------
    List[str]
        List of separate balanced groups of parentheses.

    Examples
    --------
    >>> separate_paren_groups('( ) (( )) (( )( ))')
    ['()', '(())', '(()())']
    """
    # Validate input type
    if not isinstance(paren_string, str):
        raise AssertionError("invalid inputs")

    # Validate characters
    for ch in paren_string:
        if ch not in ("(", ")", " "):
            raise AssertionError("invalid inputs")

    # Validate balanced parentheses
    cnt = 0
    for ch in paren_string:
        if ch == "(":
            cnt += 1
        elif ch == ")":
            cnt -= 1
        if cnt < 0:
            raise AssertionError("invalid inputs")
    if cnt != 0:
        raise AssertionError("invalid inputs")

    # Main logic
    groups = []
    current = []
    depth = 0
    for ch in paren_string:
        if ch == " ":
            continue
        if ch == "(":
            depth += 1
            current.append(ch)
        elif ch == ")":
            current.append(ch)
            depth -= 1
            if depth == 0:
                groups.append("".join(current))
                current = []

    return groups
