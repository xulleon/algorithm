# https://www.lintcode.com/problem/61/
# 81 ms time cost· 6.27 MB memory cost· Your submission beats 97.80 % Submissions
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer sorted array
    @param target: an integer to be inserted
    @return: a list of length 2, [index1, index2]
    """
    def search_range(self, a: List[int], target: int) -> List[int]:
        # write your code here
        n = len(a)
        if n == 0:
            return [-1, -1]
        if n == 1:
            return [-1, -1] if a[0] != target else [0, 0]

        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if a[mid] < target:
                start = mid
            else:
                end = mid

        if a[start] == target:
            pl = start
        elif a[end] == target:
            pl = end
        else:
            return [-1, -1]
        pr = pl
        while pr < n and a[pr] == target:
            pr += 1

        return [pl, pr - 1]
