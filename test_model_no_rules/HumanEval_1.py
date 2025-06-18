# HumanEval/1
from typing import List

def separate_paren_groups(paren_string: str) -> List[str]:
    s = paren_string.replace(" ", "")
    groups = []
    i = 0
    n = len(s)
    while i < n:
        if s[i] == ')':
            i += 1
            continue
        start = i
        cnt = 1
        i += 1
        while i < n and cnt != 0:
            if s[i] == '(':
                cnt += 1
            elif s[i] == ')':
                cnt -= 1
            i += 1
        groups.append(s[start:i])
    return groups

