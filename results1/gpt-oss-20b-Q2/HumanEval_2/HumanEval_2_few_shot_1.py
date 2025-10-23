def truncate_number(number: float) -> float:
    """Return the decimal part of a positive floating point number.

    The decimal part is the fractional component of the number, i.e. the
    difference between the number and its integer part (the largest integer
    smaller than or equal to the number).

    Parameters
    ----------
    number : float
        A positive floating point number.

    Returns
    -------
    float
        The decimal part of ``number``.  For an integer input the result is ``0.0``.

    Examples
    --------
    >>> truncate_number(3.5)
    0.5
    >>> truncate_number(10)
    0.0
    """
    if number < 0:
        raise ValueError("truncate_number expects a positive number")
    int_part = int(number)
    return number - int_part