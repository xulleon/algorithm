# https://www.lintcode.com/problem/14/
# 81 ms time cost· 9.91 MB memory cost· Your submission beats 100.00 % Submissions
from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array.
    @param target: Target to find.
    @return: The first position of target. Position starts from 0.
    """
    def binary_search(self, nums: List[int], target: int) -> int:
        # write your code here
        n = len(nums)
        if n == 0:
            return -1

        if n == 1:
            return 1 if nums[0] == target else -1

        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            return start

        if nums[end] == target:
            return end

        return -1

