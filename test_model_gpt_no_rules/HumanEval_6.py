from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """Input to this function is a string represented multiple groups for nested parentheses separated by spaces.
    For each of the group, output the deepest level of nesting of parentheses.
    E.g. (()()) has maximum two levels of nesting while ((())) has three.

    >>> parse_nested_parens('(()()) ((())) () ((())()())')
    [2, 3, 1, 3]
    """
    # Validate input type
    assert isinstance(paren_string, str), "invalid inputs"

    # Split the input string into groups separated by whitespace
    groups = paren_string.split()
    result: List[int] = []

    for group in groups:
        depth = 0
        max_depth = 0
        for ch in group:
            if ch == '(':
                depth += 1
                if depth > max_depth:
                    max_depth = depth
            elif ch == ')':
                depth -= 1
            else:
                # According to contract, only parentheses and spaces are allowed
                raise AssertionError("invalid inputs")
        # After processing a group, depth should be zero (balanced)
        assert depth == 0, "invalid inputs"
        result.append(max_depth)

    return result
