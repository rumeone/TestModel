from typing import List


def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """Filter an input list of strings only for ones that contain the given substring.

    Parameters
    ----------
    strings : List[str]
        The list of strings to filter.
    substring : str
        The substring to search for.

    Returns
    -------
    List[str]
        A new list containing only the strings that contain ``substring``.

    Examples
    --------
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """
    return [s for s in strings if substring in s]