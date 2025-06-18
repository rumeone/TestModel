# HumanEval/6
from typing import List

def parse_nested_parens(paren_string: str) -> List[int]:
    groups = paren_string.split()
    result = []
    for group in groups:
        if group == "":
            result.append(0)
            continue
        current = 0
        max_level = 0
        for char in group:
            if char == '(':
                current += 1
            elif char == ')':
                current -= 1
            else:
                continue
            if current > max_level:
                max_level = current
        result.append(max_level)
    return result

