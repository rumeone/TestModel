# HumanEval/10
def make_palindrome(input_string: str) -> str:
    """ Find the shortest palindrome that begins with the supplied string """
    if input_string == '':
        return ''
    for i in range(len(input_string), -1, -1):
        if input_string[:i] == is_palindrome(input_string[:i]):
            return input_string[:i] + input_string[:i-1][::-1]
    return input_string + input_string[::-1]
