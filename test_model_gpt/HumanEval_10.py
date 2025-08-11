# Module-level docstring
"""
Utility functions for palindrome operations.
"""

def is_palindrome(string: str) -> bool:
    """Return True if the given string is a palindrome."""
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """Find the shortest palindrome that begins with a supplied string.

    The algorithm finds the longest suffix of the input that is a palindrome
    and appends the reverse of the preceding prefix.
    """
    assert isinstance(string, str), "invalid inputs"
    n = len(string)
    # Find longest suffix that is a palindrome
    for i in range(n, 0, -1):
        suffix = string[i:]
        if suffix == suffix[::-1]:
            prefix = string[:i]
            return string + prefix[::-1]
    # If no suffix found (should not happen), return the string itself
    return string
