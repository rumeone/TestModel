# HumanEval/10
def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]

def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string """
    # Find the longest palindromic suffix
    for i in range(len(string), -1, -1):
        if is_palindrome(string[:i]):
            return string[:i] + string[i:][::-1]
    return string
