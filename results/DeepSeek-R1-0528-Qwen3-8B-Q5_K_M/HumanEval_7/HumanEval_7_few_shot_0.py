from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings only for ones that contain given substring.
    Args:
        strings: List of strings to be filtered.
        substring: The substring to look for in each string.
    Returns:
        A list of strings that contain the substring.
    """
    return [s for s in strings if substring in s]