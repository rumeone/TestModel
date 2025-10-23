"""
Utility functions for palindrome manipulation.
"""

def is_palindrome(string: str) -> bool:
    """Return True if the given string is a palindrome."""
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """Return the shortest palindrome that starts with *string*.

    The algorithm finds the longest postfix of *string* that is a palindrome,
    then appends the reverse of the remaining prefix.
    """
    # Find the longest postfix that is a palindrome
    longest = ""
    for i in range(len(string)):
        suffix = string[i:]
        if suffix == suffix[::-1]:
            longest = suffix

    # The prefix before the palindrome suffix
    prefix = string[:len(string) - len(longest)]
    # Append reverse of that prefix
    return string + prefix[::-1]