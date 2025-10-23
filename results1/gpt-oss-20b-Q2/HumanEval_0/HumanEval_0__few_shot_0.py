from typing import List


def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """Return ``True`` if any two distinct elements in ``numbers`` are closer than ``threshold``.

    The function checks all unordered pairs of indices and returns ``True`` as soon as a pair with
    ``abs(a - b) < threshold`` is found.  If the list has fewer than two elements, the result is ``False``.

    Examples
    --------
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
    n = len(numbers)
    if n < 2:
        return False

    for i in range(n - 1):
        a = numbers[i]
        for j in range(i + 1, n):
            if abs(a - numbers[j]) < threshold:
                return True
    return False