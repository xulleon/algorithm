# https://www.lintcode.com/problem/31/
# 67 ms time cost 5.02 MB memory cost Your submission beats 63.60 % Submissions
from typing import (
    List,
)

class Solution:
    """
    @param nums: The integer array you should partition
    @param k: An integer
    @return: The index after partition
    """
    def partition_array(self, nums: List[int], k: int) -> int:
        # write your code here
        if len(nums) < 2:
            return 0

        return self.quicksort(nums, 0, len(nums) - 1, k)

    def quicksort(self, nums, start, end, k):
        if start >= end:
            return
        
        left, right = start, end
        while left < right:
            while left <= right and nums[left] < k:
                left += 1

            while left <= right and nums[right] >= k:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
        # at this moment, the nums is divided to two parts. left size from start to right is all the integers which is less than k
        # The right part from left to end is all the integers which is >= k. Therefore, the first index at right part is the one 
        # which is >= k
        return left
