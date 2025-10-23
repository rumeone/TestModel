def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    # Find the longest palindromic suffix
    n = len(string)
    for i in range(n):
        if is_palindrome(string[i:]):
            # The prefix is the substring from start to i-1
            prefix = string[:i]
            # Return the prefix + the original string
            return prefix + string[::-1]
    # If no palindromic suffix is found, return the string plus its reverse
    return string + string[::-1]