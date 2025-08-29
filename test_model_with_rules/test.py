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


# HumanEval_0
def test_has_close_elements_case1():
    assert has_close_elements([1.0, 1.1, 2.2], 0.15)
def test_has_close_elements_case2():
    assert not has_close_elements([1.0, 2.0, 3.0], 0.5)
def test_has_close_elements_case3():
    assert not has_close_elements([], 0.1)


# HumanEval_1
def test_separate_paren_groups_case1():
    assert separate_paren_groups("(())()") == ["(())", "()"]
def test_separate_paren_groups_case2():
    assert separate_paren_groups("()") == ["()"]
def test_separate_paren_groups_case3():
    with pytest.raises(ValueError):
        separate_paren_groups("())")


# HumanEval_2
def test_truncate_number_case1():
    assert truncate_number(3.5) == 0.5
def test_truncate_number_case2():
    assert truncate_number(7.0) == 0.0
def test_truncate_number_case3():
    with pytest.raises(AssertionError):
        truncate_number(-1.2)


# HumanEval_3
def test_below_zero_case1():
    assert below_zero([1, 2, -5])
def test_below_zero_case2():
    assert not below_zero([3, -1, -1])
def test_below_zero_case3():
    assert not below_zero([])


# HumanEval_4
def test_mean_absolute_deviation_case1():
    assert mean_absolute_deviation([1.0, 2.0, 3.0]) == pytest.approx(0.6667, rel=1e-3)
def test_mean_absolute_deviation_case2():
    assert mean_absolute_deviation([5.0, 5.0, 5.0]) == 0.0
def test_mean_absolute_deviation_case3():
    with pytest.raises(AssertionError):
        mean_absolute_deviation([])


# HumanEval_5
def test_intersperse_case1():
    assert intersperse([1, 2, 3], 0) == [1, 0, 2, 0, 3]
def test_intersperse_case2():
    assert intersperse([], 5) == []
def test_intersperse_case3():
    assert intersperse([7], 9) == [7]


# HumanEval_6
def test_parse_nested_parens_case1():
    assert parse_nested_parens("(()) ((())) ()") == [2, 3, 1]
def test_parse_nested_parens_case2():
    assert parse_nested_parens("((()))") == [3]
def test_parse_nested_parens_case3():
    assert parse_nested_parens("() ()") == [1, 1]


# HumanEval_7
def test_filter_by_substring_case1():
    assert filter_by_substring(["abc", "def", "ab"], "ab") == ["abc", "ab"]
def test_filter_by_substring_case2():
    assert filter_by_substring(["one", "two"], "z") == []
def test_filter_by_substring_case3():
    assert filter_by_substring(["", "a"], "") == ["", "a"]


# HumanEval_8
def test_sum_product_case1():
    assert sum_product([1, 2, 3]) == (6, 6)
def test_sum_product_case2():
    assert sum_product([]) == (0, 1)
def test_sum_product_case3():
    assert sum_product([5]) == (5, 5)


# HumanEval_9
def test_rolling_max_case1():
    assert rolling_max([1, 2, 3, 2]) == [1, 2, 3, 3]
def test_rolling_max_case2():
    assert rolling_max([3, 1, 2]) == [3, 3, 3]
def test_rolling_max_case3():
    assert rolling_max([]) == []


# HumanEval_10
def test_make_palindrome_case1():
    result = make_palindrome("abc")
    assert result.startswith("abc") and is_palindrome(result)
def test_make_palindrome_case2():
    result = make_palindrome("race")
    assert result.startswith("race") and is_palindrome(result)
def test_make_palindrome_case3():
    assert make_palindrome("") == ""


# HumanEval_11
def test_string_xor_case1():
    assert string_xor("101", "010") == "111"
def test_string_xor_case2():
    assert string_xor("111", "000") == "111"
def test_string_xor_case3():
    with pytest.raises(AssertionError):
        string_xor("10", "1")


# HumanEval_12
def test_longest_case1():
    assert longest(["a", "abc", "ab"]) == "abc"
def test_longest_case2():
    assert longest([]) is None
def test_longest_case3():
    assert longest(["same", "same"]) == "same"


# HumanEval_13
def test_greatest_common_divisor_case1():
    assert greatest_common_divisor(12, 8) == 4
def test_greatest_common_divisor_case2():
    assert greatest_common_divisor(7, 3) == 1
def test_greatest_common_divisor_case3():
    assert greatest_common_divisor(100, 25) == 25


# HumanEval_14
def test_all_prefixes_case1():
    assert all_prefixes("abc") == ["a", "ab", "abc"]
def test_all_prefixes_case2():
    assert all_prefixes("x") == ["x"]
def test_all_prefixes_case3():
    assert all_prefixes("") == []


if __name__ == "__main__":
    pytest.main([__file__])
