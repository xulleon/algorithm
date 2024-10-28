# https://www.lintcode.com/problem/585/description
# SOLUTION 1
# 81 ms time cost· 6.20 MB memory cost· Your submission beats 98.60 % Submissions
from typing import (
    List,
)

class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountain_sequence(self, nums: List[int]) -> int:
        # write your code here
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return nums[0]

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                return nums[i]
        return -1

# SOLUTION 2
# 81 ms time cost· 6.18 MB memory cost· Your submission beats 98.60 % Submissions
class Solution:
    """
    @param nums: a mountain sequence which increase firstly and then decrease
    @return: then mountain top
    """
    def mountain_sequence(self, nums: List[int]) -> int:
        # write your code here
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return nums[0]

        start, end = 0, n - 1
        ind = 0
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[mid + 1]:
                end = mid

            if nums[mid] < nums[mid + 1]:
                start = mid

        return max(nums[start], nums[end])
