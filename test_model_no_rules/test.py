from typing import List
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
from HumanEval_11 import string_xor
from HumanEval_12 import longest
from HumanEval_13 import greatest_common_divisor
from HumanEval_14 import all_prefixes


# -------- has_close_elements --------
def test_has_close_elements_true():
    assert has_close_elements([1.0, 1.1, 2.5], 0.2) is True

def test_has_close_elements_false():
    assert has_close_elements([1.0, 2.0, 3.0], 0.5) is False

def test_has_close_elements_single():
    assert has_close_elements([5.0], 0.1) is False


# -------- separate_paren_groups --------
def test_separate_paren_groups_basic():
    assert separate_paren_groups("(()) ()") == ["(())", "()"]

def test_separate_paren_groups_multiple():
    assert separate_paren_groups("()()") == ["()", "()"]

def test_separate_paren_groups_nested():
    assert separate_paren_groups("(())") == ["(())"]


# -------- truncate_number --------
def test_truncate_number_fractional():
    assert truncate_number(3.14) == pytest.approx(0.14, rel=1e-9)

def test_truncate_number_integer():
    assert truncate_number(7.0) == 0.0

def test_truncate_number_negative():
    assert truncate_number(-5.75) == pytest.approx(0.25, rel=1e-9)


# -------- below_zero --------
def test_below_zero_true():
    assert below_zero([10, -15, 5]) is True

def test_below_zero_false():
    assert below_zero([5, 5, -3]) is False

def test_below_zero_single_negative():
    assert below_zero([-1]) is True


# -------- mean_absolute_deviation --------
def test_mean_absolute_deviation_simple():
    nums = [1.0, 2.0, 3.0]
    mean = 2.0
    expected = sum(abs(x - mean) for x in nums) / 3
    assert mean_absolute_deviation(nums) == pytest.approx(expected, rel=1e-9)

def test_mean_absolute_deviation_identical():
    nums = [5.0, 5.0, 5.0]
    assert mean_absolute_deviation(nums) == 0.0

def test_mean_absolute_deviation_empty():
    assert mean_absolute_deviation([]) == 0.0


# -------- intersperse --------
def test_intersperse_basic():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]

def test_intersperse_single():
    assert intersperse([42], 9) == [42]

def test_intersperse_empty():
    assert intersperse([], 7) == []


# -------- parse_nested_parens --------
def test_parse_nested_parens_basic():
    assert parse_nested_parens("(()) ()") == [2, 1]

def test_parse_nested_parens_multiple():
    assert parse_nested_parens("() (()) (()())") == [1, 2, 2]

def test_parse_nested_parens_single():
    assert parse_nested_parens("((()))") == [3]


# -------- filter_by_substring --------
def test_filter_by_substring_found():
    assert filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']

def test_filter_by_substring_none():
    assert filter_by_substring(['hello', 'world'], 'x') == []

def test_filter_by_substring_empty_list():
    assert filter_by_substring([], 'a') == []


# -------- sum_product --------
def test_sum_product_basic():
    assert sum_product([1, 2, 3]) == (6, 6)

def test_sum_product_empty():
    assert sum_product([]) == (0, 1)

def test_sum_product_negative():
    assert sum_product([-1, 2]) == (1, -2)


# -------- rolling_max --------
def test_rolling_max_increasing():
    assert rolling_max([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_rolling_max_decreasing():
    assert rolling_max([5, 4, 3, 2]) == [5, 5, 5, 5]

def test_rolling_max_mixed():
    assert rolling_max([1, 3, 2, 4]) == [1, 3, 3, 4]


# -------- string_xor --------
def test_string_xor_basic():
    assert string_xor("101", "110") == "011"

def test_string_xor_all_equal():
    assert string_xor("111", "111") == "000"

def test_string_xor_alternating():
    assert string_xor("1010", "0101") == "1111"


# -------- longest --------
def test_longest_basic():
    assert longest(["a", "ab", "abc"]) == "abc"

def test_longest_equal_length():
    assert longest(["aa", "bb", "cc"]) == "aa"

def test_longest_empty():
    assert longest([]) is None


# -------- gcd --------
def test_gcd_basic():
    assert greatest_common_divisor(12, 8) == 4

def test_gcd_coprime():
    assert greatest_common_divisor(17, 13) == 1

def test_gcd_one_zero():
    assert greatest_common_divisor(0, 5) == 5


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



