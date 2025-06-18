# HumanEval/8
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """Return a tuple with the sum and product of all integers in the list.
    
    Args:
        numbers: List of integers to calculate sum and product for.
        
    Returns:
        Tuple containing the sum and product of the numbers.
        
    Note:
        For an empty list, sum is 0 and product is 1.
    """
    total = 0
    product = 1
    for num in numbers:
        total += num
        product *= num
    return (total, product)
