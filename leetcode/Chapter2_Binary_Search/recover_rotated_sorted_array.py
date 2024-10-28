# https://www.lintcode.com/problem/39/record
# 81 ms time cost· 4.97 MB memory cost· Your submission beats 92.20 % Submissions
from typing import (
    List,
)

class Solution:
    """
    @param nums: An integer array
    @return: nothing
    """
    def recover_rotated_sorted_array(self, nums: List[int]):
        # write your code here
        n = len(nums)
        if n < 2:
            return nums

        # if it is a regular sorted array, then return itself
        if nums[n - 1] > nums[0]:
            return nums

        i = 0
        while i < n - 1 and nums[i] <= nums[i + 1]:
            i += 1

        self.flip(nums, 0, i)
        self.flip(nums, i + 1, n - 1)
        self.flip(nums, 0, n - 1)

        return nums
