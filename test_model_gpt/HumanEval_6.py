from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    """Parse groups of parentheses separated by spaces and return the maximum nesting depth for each group."""
    groups = paren_string.split()
    depths = []
    for group in groups:
        max_depth = 0
        current = 0
        for ch in group:
            if ch == "(":
                current += 1
                if current > max_depth:
                    max_depth = current
            elif ch == ")":
                current -= 1
        depths.append(max_depth)
    return depths
