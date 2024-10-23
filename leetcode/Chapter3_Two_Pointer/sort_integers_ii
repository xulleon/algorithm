# https://www.lintcode.com/problem/464/
#
from typing import (
    List,
)

class Solution:
    """
    @param a: an integer array
    @return: nothing
    """
    def sort_integers2(self, a: List[int]):
        # write your code here
        n = len(a)
        if n == 0:
            return []

        start, end = 0, n - 1
        self.quicksort(a, 0, n - 1)
        return a

    def quicksort(self, nums, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1

            while left <= right and nums[right] > pivot:
                right -= 1

            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        self.quicksort(nums, start, right)
        self.quicksort(nums, left, end)
