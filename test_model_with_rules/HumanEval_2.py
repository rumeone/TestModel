# HumanEval/2
def truncate_number(number: float) -> float:
    """Given a positive floating point number, decompose it into an integer part and decimals, then return the decimal part."""
    assert number > 0, "invalid inputs"
    assert isinstance(number, float), "invalid inputs"
    assert number != float("+inf"), "invalid inputs"
    return number % 1.0
