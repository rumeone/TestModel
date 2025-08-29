import pytest
from HumanEval_0 import has_close_elements
from HumanEval_1 import separate_paren_groups
from HumanEval_2 import truncate_number
from HumanEval_3 import below_zero
from HumanEval_4 import mean_absolute_deviation
from HumanEval_5 import intersperse
from HumanEval_6 import parse_nested_parens
from HumanEval_7 import filter_by_substring
from HumanEval_8 import sum_product
from HumanEval_9 import rolling_max
from HumanEval_10 import is_palindrome, make_palindrome
from HumanEval_11 import string_xor
from HumanEval_12 import longest
from HumanEval_13 import greatest_common_divisor
from HumanEval_14 import all_prefixes

# -------- has_close_elements --------
def test_has_close_elements_true():
    assert has_close_elements([1.0, 1.05, 2.0], 0.1) is True

def test_has_close_elements_false():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) is False

def test_has_close_elements_single():
    assert has_close_elements([5.0], 0.1) is False

# -------- separate_paren_groups --------
def test_separate_paren_groups_basic():
    assert separate_paren_groups("( ) (( ))") == ["()", "(())"]

def test_separate_paren_groups_nested():
    assert separate_paren_groups("((()))") == ["((()))"]

def test_separate_paren_groups_multiple():
    assert separate_paren_groups("(()) () (())") == ["(())", "()", "(())"]

# -------- truncate_number --------
def test_truncate_number_half():
    assert truncate_number(3.5) == 0.5

def test_truncate_number_integer():
    assert truncate_number(7.0) == 0.0

def test_truncate_number_small_decimal():
    assert truncate_number(2.123) == pytest.approx(0.123, rel=1e-9)

# -------- below_zero --------
def test_below_zero_true():
    assert below_zero([10, -15, 5]) is True

def test_below_zero_false():
    assert below_zero([5, -2, 3]) is False

def test_below_zero_empty():
    assert below_zero([]) is False

# -------- mean_absolute_deviation --------
def test_mean_absolute_deviation_basic():
    assert mean_absolute_deviation([1.0, 2.0, 3.0]) == pytest.approx(2/3, rel=1e-9)

def test_mean_absolute_deviation_all_equal():
    assert mean_absolute_deviation([4.0, 4.0, 4.0]) == 0.0

def test_mean_absolute_deviation_two_numbers():
    assert mean_absolute_deviation([1.0, 5.0]) == 2.0

# -------- intersperse --------
def test_intersperse_empty():
    assert intersperse([], 7) == []

def test_intersperse_basic():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

def test_intersperse_single():
    assert intersperse([5], 9) == [5]

# -------- parse_nested_parens --------
def test_parse_nested_parens_basic():
    assert parse_nested_parens("(()) ()") == [2, 1]

def test_parse_nested_parens_nested():
    assert parse_nested_parens("(((())))") == [4]

def test_parse_nested_parens_multiple():
    assert parse_nested_parens("() (()) ((()))") == [1, 2, 3]

# -------- filter_by_substring --------
def test_filter_by_substring_some():
    assert filter_by_substring(["apple", "banana", "apricot"], "ap") == ["apple", "apricot"]

def test_filter_by_substring_none():
    assert filter_by_substring(["cat", "dog"], "z") == []

def test_filter_by_substring_all():
    assert filter_by_substring(["x", "xx", "xxx"], "x") == ["x", "xx", "xxx"]

# -------- sum_product --------
def test_sum_product_basic():
    assert sum_product([1, 2, 3]) == (6, 6)

def test_sum_product_empty():
    assert sum_product([]) == (0, 1)

def test_sum_product_single():
    assert sum_product([7]) == (7, 7)

# -------- rolling_max --------
def test_rolling_max_basic():
    assert rolling_max([1, 3, 2, 5]) == [1, 3, 3, 5]

def test_rolling_max_monotonic():
    assert rolling_max([1, 2, 3]) == [1, 2, 3]

def test_rolling_max_descending():
    assert rolling_max([5, 4, 3]) == [5, 5, 5]

# -------- make_palindrome --------
def test_make_palindrome_already_palindrome():
    assert make_palindrome("madam") == "madam"

def test_make_palindrome_extend():
    assert make_palindrome("race") == "racecar"

def test_make_palindrome_single():
    assert make_palindrome("a") == "a"

# -------- string_xor --------
def test_string_xor_basic():
    assert string_xor("010", "110") == "100"

def test_string_xor_same():
    assert string_xor("111", "111") == "000"

def test_string_xor_opposite():
    assert string_xor("000", "111") == "111"

# -------- longest --------
def test_longest_basic():
    assert longest(["a", "abc", "ab"]) == "abc"

def test_longest_equal():
    assert longest(["xx", "yy"]) in ["xx", "yy"]

def test_longest_empty():
    assert longest([]) is None

# -------- greatest_common_divisor --------
def test_gcd_basic():
    assert greatest_common_divisor(12, 18) == 6

def test_gcd_prime():
    assert greatest_common_divisor(7, 13) == 1

def test_gcd_equal():
    assert greatest_common_divisor(9, 9) == 9

# -------- all_prefixes --------
def test_all_prefixes_basic():
    assert all_prefixes("abc") == ["a", "ab", "abc"]

def test_all_prefixes_single():
    assert all_prefixes("x") == ["x"]

def test_all_prefixes_empty():
    assert all_prefixes("") == []


if __name__ == "__main__":
    import pytest
    pytest.main([__file__])