def truncate_number(number: float) -> float:
    """Given a positive floating point number, decompose into integer part and decimals.
    Return the decimal part of the number.

    Args:
        number (float): A positive floating point number.

    Returns:
        float: The decimal part of the number.
    """
    return number % 1.0