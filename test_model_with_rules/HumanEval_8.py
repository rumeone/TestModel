# HumanEval/8
from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    """
    total = 0
    product = 1
    for num in numbers:
        total += num
        product *= num
    return (total, product)
