from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """Parse a string of parenthesis groups separated by spaces and return the maximum nesting depth for each group.

    Parameters
    ----------
    paren_string : str
        A string containing groups of parentheses separated by spaces. Each group may contain only '(' and ')' characters.

    Returns
    -------
    List[int]
        A list of integers where each integer corresponds to the maximum depth of nested parentheses in the respective group.

    Examples
    --------
    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    if not paren_string:
        return []

    # Split the input into groups separated by whitespace
    groups = paren_string.split()
    depths: List[int] = []

    for group in groups:
        current_depth = 0
        max_depth = 0
        for ch in group:
            if ch == '(':
                current_depth += 1
                if current_depth > max_depth:
                    max_depth = current_depth
            elif ch == ')':
                current_depth -= 1
                # If the string is malformed, current_depth could become negative.
                # We ignore such cases as the specification assumes well‑formed input.
        depths.append(max_depth)

    return depths