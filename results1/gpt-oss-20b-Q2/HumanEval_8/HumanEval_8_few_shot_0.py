from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """Return a tuple of the sum and product of all integers in *numbers*.

    The sum of an empty list is 0 and the product is 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """
    total_sum = 0
    total_prod = 1
    for n in numbers:
        total_sum += n
        total_prod *= n
    return total_sum, total_prod