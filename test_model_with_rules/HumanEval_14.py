from typing import List

# HumanEval/14
def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string """
    return [string[:i] for i in range(1, len(string)+1)]
