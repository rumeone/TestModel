from typing import List

# HumanEval/5
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers'."""
    result = []
    for num in numbers:
        result.append(num)
        if result[-1] != numbers[-1]:
            result.append(delimeter)
    return result
