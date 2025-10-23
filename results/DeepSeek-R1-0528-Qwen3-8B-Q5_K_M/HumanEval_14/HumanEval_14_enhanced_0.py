from typing import List


def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """
    # Initialize an empty list to store the prefixes
    prefixes = []
    # Loop through each index in the string to get the prefix at that position
    for i in range(len(string)):
        # Add the substring from the start to the current index (inclusive) to the list
        prefixes.append(string[:i+1])
    # Return the list of prefixes
    return prefixes