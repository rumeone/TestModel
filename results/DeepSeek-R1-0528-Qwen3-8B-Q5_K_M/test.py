from typing import List

from HumanEval_0.HumanEval_0_baseline_0 import has_close_elements as has_close_elements_b
from HumanEval_0.HumanEval_0_enhanced_0 import has_close_elements as has_close_elements_e
from HumanEval_0.HumanEval_0_few_shot_1 import has_close_elements as has_close_elements_f

from HumanEval_1.HumanEval_1_baseline_0 import separate_paren_groups as separate_paren_groups_b
from HumanEval_1.HumanEval_1_enhanced_1 import separate_paren_groups as separate_paren_groups_e
from HumanEval_1.HumanEval_1_few_shot_1 import separate_paren_groups as separate_paren_groups_f

from HumanEval_2.HumanEval_2_baseline_0 import truncate_number as truncate_number_b
from HumanEval_2.HumanEval_2_enhanced_0 import truncate_number as truncate_number_e
from HumanEval_2.HumanEval_2_few_shot_0 import truncate_number as truncate_number_f

from HumanEval_3.HumanEval_3_baseline_0 import below_zero as below_zero_b
from HumanEval_3.HumanEval_3_enhanced_1 import below_zero as below_zero_e
from HumanEval_3.HumanEval_3_few_shot_0 import below_zero as below_zero_f

from HumanEval_4.HumanEval_4_baseline_1 import mean_absolute_deviation as mean_absolute_deviation_b
from HumanEval_4.HumanEval_4_enhanced_1 import mean_absolute_deviation as mean_absolute_deviation_e
from HumanEval_4.HumanEval_4_few_shot_1 import mean_absolute_deviation as mean_absolute_deviation_f

from HumanEval_5.HumanEval_5_baseline_0 import intersperse as intersperse_b
from HumanEval_5.HumanEval_5_enhanced_0 import intersperse as intersperse_e
from HumanEval_5.HumanEval_5_few_shot_1 import intersperse as intersperse_f

from HumanEval_6.HumanEval_6_baseline_0 import parse_nested_preps as parse_nested_parens_b
from HumanEval_6.HumanEval_6_enhanced_0 import parse_nested_parens as parse_nested_parens_e
from HumanEval_6.HumanEval_6_few_shot_0 import parse_nested_parens as parse_nested_parens_f

from HumanEval_7.HumanEval_7_baseline_0 import filter_by_substring as filter_by_substring_b
from HumanEval_7.HumanEval_7_enhanced_0 import filter_by_substring as filter_by_substring_e
from HumanEval_7.HumanEval_7_few_shot_0 import filter_by_substring as filter_by_substring_f

from HumanEval_8.HumanEval_8_baseline_1 import sum_product as sum_product_b
from HumanEval_8.HumanEval_8_enhanced_0 import sum_product as sum_product_e
from HumanEval_8.HumanEval_8_few_shot_1 import sum_product as sum_product_f

from HumanEval_9.HumanEval_9_baseline_0 import rolling_max as rolling_max_b
from HumanEval_9.HumanEval_9_enhanced_0 import rolling_max as rolling_max_e
from HumanEval_9.HumanEval_9_few_shot_1 import rolling_max as rolling_max_f

from HumanEval_10.HumanEval_10_baseline_0 import is_palindrome as is_palindrome_b, make_palindrome as make_palindrome_b
from HumanEval_10.HumanEval_10_enhanced_0 import is_palindrome as is_palindrome_e, make_palindrome as make_palindrome_e
from HumanEval_10.HumanEval_10_few_shot_1 import is_palindrome as is_palindrome_f, make_palindrome as make_palindrome_f

from HumanEval_11.HumanEval_11_baseline_1 import string_xor as string_xor_b
from HumanEval_11.HumanEval_11_enhanced_1 import string_xor as string_xor_e
from HumanEval_11.HumanEval_11_few_shot_0 import string_xor as string_xor_f

from HumanEval_12.HumanEval_12_baseline_1 import longest as longest_b
from HumanEval_12.HumanEval_12_enhanced_0 import longest as longest_e
from HumanEval_12.HumanEval_12_few_shot_1 import longest as longest_f

from HumanEval_13.HumanEval_13_baseline_0 import greatest_common_divisor as greatest_common_divisor_b
from HumanEval_13.HumanEval_13_enhanced_0 import greatest_common_divisor as greatest_common_divisor_e
from HumanEval_13.HumanEval_13_few_shot_0 import greatest_common_divisor as greatest_common_divisor_f

from HumanEval_14.HumanEval_14_baseline_0 import all_prefixes as all_prefixes_b
from HumanEval_14.HumanEval_14_enhanced_0 import all_prefixes as all_prefixes_e
from HumanEval_14.HumanEval_14_few_shot_0 import all_prefixes as all_prefixes_f



import pytest

# ======= Has close elements (HumanEval_0) already present in imports =======
def test_has_close_elements_b():
    assert has_close_elements_b([1.0, 1.05, 2.0], 0.1) is True
    assert has_close_elements_b([1.0, 2.0, 3.0], 0.5) is False
    assert has_close_elements_b([5.0], 0.1) is False

def test_has_close_elements_e():
    assert has_close_elements_e([1.0, 1.05, 2.0], 0.1) is True
    assert has_close_elements_e([1.0, 2.0, 3.0], 0.5) is False
    assert has_close_elements_e([5.0], 0.1) is False

def test_has_close_elements_f():
    assert has_close_elements_f([1.0, 1.05, 2.0], 0.1) is True
    assert has_close_elements_f([1.0, 2.0, 3.0], 0.5) is False
    assert has_close_elements_f([5.0], 0.1) is False


# ======= separate_paren_groups (HumanEval_1) =======
def test_separate_paren_groups_b():
    assert separate_paren_groups_b("( ) (( ))") == ["()", "(())"]
    assert separate_paren_groups_b("((()))") == ["((()))"]
    assert separate_paren_groups_b("(()) () (())") == ["(())", "()", "(())"]

def test_separate_paren_groups_e():
    assert separate_paren_groups_e("( ) (( ))") == ["()", "(())"]
    assert separate_paren_groups_e("((()))") == ["((()))"]
    assert separate_paren_groups_e("(()) () (())") == ["(())", "()", "(())"]

def test_separate_paren_groups_f():
    assert separate_paren_groups_f("( ) (( ))") == ["()", "(())"]
    assert separate_paren_groups_f("((()))") == ["((()))"]
    assert separate_paren_groups_f("(()) () (())") == ["(())", "()", "(())"]


# ======= truncate_number (HumanEval_2) =======
def test_truncate_number_b():
    assert truncate_number_b(3.5) == 0.5
    assert truncate_number_b(7.0) == 0.0
    assert truncate_number_b(2.123) == pytest.approx(0.123, rel=1e-9)

def test_truncate_number_e():
    assert truncate_number_e(3.5) == 0.5
    assert truncate_number_e(7.0) == 0.0
    assert truncate_number_e(2.123) == pytest.approx(0.123, rel=1e-9)

def test_truncate_number_f():
    assert truncate_number_f(3.5) == 0.5
    assert truncate_number_f(7.0) == 0.0
    assert truncate_number_f(2.123) == pytest.approx(0.123, rel=1e-9)


# ======= below_zero (HumanEval_3) =======
def test_below_zero_b():
    assert below_zero_b([10, -15, 5]) is True
    assert below_zero_b([5, -2, 3]) is False
    assert below_zero_b([]) is False

def test_below_zero_e():
    assert below_zero_e([10, -15, 5]) is True
    assert below_zero_e([5, -2, 3]) is False
    assert below_zero_e([]) is False

def test_below_zero_f():
    assert below_zero_f([10, -15, 5]) is True
    assert below_zero_f([5, -2, 3]) is False
    assert below_zero_f([]) is False


# ======= mean_absolute_deviation (HumanEval_4) =======
def test_mean_absolute_deviation_b():
    assert mean_absolute_deviation_b([1.0, 2.0, 3.0]) == pytest.approx(2/3, rel=1e-9)
    assert mean_absolute_deviation_b([4.0, 4.0, 4.0]) == 0.0
    assert mean_absolute_deviation_b([1.0, 5.0]) == 2.0

def test_mean_absolute_deviation_e():
    assert mean_absolute_deviation_e([1.0, 2.0, 3.0]) == pytest.approx(2/3, rel=1e-9)
    assert mean_absolute_deviation_e([4.0, 4.0, 4.0]) == 0.0
    assert mean_absolute_deviation_e([1.0, 5.0]) == 2.0

def test_mean_absolute_deviation_f():
    assert mean_absolute_deviation_f([1.0, 2.0, 3.0]) == pytest.approx(2/3, rel=1e-9)
    assert mean_absolute_deviation_f([4.0, 4.0, 4.0]) == 0.0
    assert mean_absolute_deviation_f([1.0, 5.0]) == 2.0


# ======= intersperse (HumanEval_5) =======
def test_intersperse_b():
    assert intersperse_b([], 7) == []
    assert intersperse_b([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert intersperse_b([5], 9) == [5]

def test_intersperse_e():
    assert intersperse_e([], 7) == []
    assert intersperse_e([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert intersperse_e([5], 9) == [5]

def test_intersperse_f():
    assert intersperse_f([], 7) == []
    assert intersperse_f([1, 2, 3], 0) == [1, 0, 2, 0, 3]
    assert intersperse_f([5], 9) == [5]


# ======= parse_nested_parens (HumanEval_6) =======
def test_parse_nested_parens_b():
    assert parse_nested_parens_b("(()) ()") == [2, 1]
    assert parse_nested_parens_b("(((())))") == [4]
    assert parse_nested_parens_b("() (()) ((()))") == [1, 2, 3]

def test_parse_nested_parens_e():
    assert parse_nested_parens_e("(()) ()") == [2, 1]
    assert parse_nested_parens_e("(((())))") == [4]
    assert parse_nested_parens_e("() (()) ((()))") == [1, 2, 3]

def test_parse_nested_parens_f():
    assert parse_nested_parens_f("(()) ()") == [2, 1]
    assert parse_nested_parens_f("(((())))") == [4]
    assert parse_nested_parens_f("() (()) ((()))") == [1, 2, 3]


# ======= filter_by_substring (HumanEval_7) =======
def test_filter_by_substring_b():
    assert filter_by_substring_b(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    assert filter_by_substring_b(['hello', 'world'], 'x') == []
    assert filter_by_substring_b([], 'a') == []

def test_filter_by_substring_e():
    assert filter_by_substring_e(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    assert filter_by_substring_e(['hello', 'world'], 'x') == []
    assert filter_by_substring_e([], 'a') == []

def test_filter_by_substring_f():
    assert filter_by_substring_f(['abc', 'bacd', 'cde', 'array'], 'a') == ['abc', 'bacd', 'array']
    assert filter_by_substring_f(['hello', 'world'], 'x') == []
    assert filter_by_substring_f([], 'a') == []


# ======= sum_product (HumanEval_8) =======
def test_sum_product_b():
    assert sum_product_b([1, 2, 3]) == (6, 6)
    assert sum_product_b([]) == (0, 1)
    assert sum_product_b([7]) == (7, 7)

def test_sum_product_e():
    assert sum_product_e([1, 2, 3]) == (6, 6)
    assert sum_product_e([]) == (0, 1)
    assert sum_product_e([7]) == (7, 7)

def test_sum_product_f():
    assert sum_product_f([1, 2, 3]) == (6, 6)
    assert sum_product_f([]) == (0, 1)
    assert sum_product_f([7]) == (7, 7)


# ======= rolling_max (HumanEval_9) =======
def test_rolling_max_b():
    assert rolling_max_b([1, 3, 2, 5]) == [1, 3, 3, 5]
    assert rolling_max_b([1, 2, 3]) == [1, 2, 3]
    assert rolling_max_b([5, 4, 3]) == [5, 5, 5]

def test_rolling_max_e():
    assert rolling_max_e([1, 3, 2, 5]) == [1, 3, 3, 5]
    assert rolling_max_e([1, 2, 3]) == [1, 2, 3]
    assert rolling_max_e([5, 4, 3]) == [5, 5, 5]

def test_rolling_max_f():
    assert rolling_max_f([1, 3, 2, 5]) == [1, 3, 3, 5]
    assert rolling_max_f([1, 2, 3]) == [1, 2, 3]
    assert rolling_max_f([5, 4, 3]) == [5, 5, 5]


# ======= is_palindrome / make_palindrome (HumanEval_10) =======
def test_is_make_palindrome_b():
    assert is_palindrome_b("madam") is True
    assert is_palindrome_b("race") is False
    assert make_palindrome_b("race") == "racecar"
    assert make_palindrome_b("a") == "a"

def test_is_make_palindrome_e():
    assert is_palindrome_e("madam") is True
    assert is_palindrome_e("race") is False
    assert make_palindrome_e("race") == "racecar"
    assert make_palindrome_e("a") == "a"

def test_is_make_palindrome_f():
    assert is_palindrome_f("madam") is True
    assert is_palindrome_f("race") is False
    assert make_palindrome_f("race") == "racecar"
    assert make_palindrome_f("a") == "a"


# ======= string_xor (HumanEval_11) =======
def test_string_xor_b():
    assert string_xor_b("010", "110") == "100"
    assert string_xor_b("111", "111") == "000"
    assert string_xor_b("000", "111") == "111"

def test_string_xor_e():
    assert string_xor_e("010", "110") == "100"
    assert string_xor_e("111", "111") == "000"
    assert string_xor_e("000", "111") == "111"

def test_string_xor_f():
    assert string_xor_f("010", "110") == "100"
    assert string_xor_f("111", "111") == "000"
    assert string_xor_f("000", "111") == "111"


# ======= longest (HumanEval_12) =======
def test_longest_b():
    assert longest_b(["a", "abc", "ab"]) == "abc"
    assert longest_b(["xx", "yy"]) in ["xx", "yy"]
    assert longest_b([]) is None

def test_longest_e():
    assert longest_e(["a", "abc", "ab"]) == "abc"
    assert longest_e(["xx", "yy"]) in ["xx", "yy"]
    assert longest_e([]) is None

def test_longest_f():
    assert longest_f(["a", "abc", "ab"]) == "abc"
    assert longest_f(["xx", "yy"]) in ["xx", "yy"]
    assert longest_f([]) is None


# ======= greatest_common_divisor (HumanEval_13) =======
def test_gcd_b():
    assert greatest_common_divisor_b(12, 18) == 6
    assert greatest_common_divisor_b(7, 13) == 1
    assert greatest_common_divisor_b(9, 9) == 9

def test_gcd_e():
    assert greatest_common_divisor_e(12, 18) == 6
    assert greatest_common_divisor_e(7, 13) == 1
    assert greatest_common_divisor_e(9, 9) == 9

def test_gcd_f():
    assert greatest_common_divisor_f(12, 18) == 6
    assert greatest_common_divisor_f(7, 13) == 1
    assert greatest_common_divisor_f(9, 9) == 9


# ======= all_prefixes (HumanEval_14) =======
def test_all_prefixes_b():
    assert all_prefixes_b("abc") == ["a", "ab", "abc"]
    assert all_prefixes_b("x") == ["x"]
    assert all_prefixes_b("") == []

def test_all_prefixes_e():
    assert all_prefixes_e("abc") == ["a", "ab", "abc"]
    assert all_prefixes_e("x") == ["x"]
    assert all_prefixes_e("") == []

def test_all_prefixes_f():
    assert all_prefixes_f("abc") == ["a", "ab", "abc"]
    assert all_prefixes_f("x") == ["x"]
    assert all_prefixes_f("") == []


if __name__ == "__main__":
    pytest.main([__file__])




