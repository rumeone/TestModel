from typing import List

# HumanEval/5
def intersperse(numbers: List[int], delimeter: int) -> List[int]:
    """Insert a number 'delimeter' between every two consecutive elements of input list `numbers'."""
    if not numbers:
        return []
    result = []
    for num in numbers:
        result.append(num)
        result.append(delimeter)
    # Remove the last added delimeter since it's not needed after the last element
    result.pop()
    return result


# Example usage:
# intersperse([1, 2, 3], 4) returns [1, 4, 2, 4, 3]
