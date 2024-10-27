# https://www.lintcode.com/problem/49/
# 81 ms time cost· 5.11 MB memory cost· Your submission beats 84.80 % Submissions
from typing import (
    List,
)

class Solution:
    """
    @param chars: The letter array you should sort by Case
    @return: nothing
    """
    def sort_letters(self, chars: List[str]):
        # write your code here
        n = len(chars)
        if n < 2:
            return chars
        pl, pr = 0, n - 1
        while pl < pr:
            # Find the first index of upper case from left
            while pl < n and 97 <= ord(chars[pl]) <= 122:
                pl += 1

            # Fidn the first index of lower case from right
            while pr >= 0 and 65 <= ord(chars[pr]) <= 90:
                    pr -= 1

            if pl < pr:
                chars[pl], chars[pr] = chars[pr], chars[pl]
                pl += 1
                pr -= 1

        return chars
