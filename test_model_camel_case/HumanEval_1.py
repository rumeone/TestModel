# HumanEval/1
from typing import List

def separateParenGroups(parenString: str) -> List[str]:
    """Separates groups of nested parentheses into balanced strings and returns a list."""
    parenString = parenString.replace(" ", "")
    result = []
    start = 0
    current = 0
    for i in range(len(parenString)):
        if parenString[i] == '(':
            current += 1
            start = i
        elif parenString[i] == ')':
            if current > 0:
                current -= 1
                if current == 0:
                    result.append(parenString[start:i+1])
            else:
                current -= 1
    return result
