# https://www.lintcode.com/problem/600/
# 81 ms time cost· 5.20 MB memory cost· Your submission beats 100.00 % Submissions
"""
The solution is to find the rectangle's low, high and left and right
"""
from typing import (
    List,
)

class Solution:
    """
    @param image: a binary matrix with '0' and '1'
    @param x: the location of one of the black pixels
    @param y: the location of one of the black pixels
    @return: an integer
    """
    def min_area(self, image: List[List[str]], x: int, y: int) -> int:
        # write your code here
        n, m = len(image), len(image[0])
        if n == 0 or m == 0:
            return 0

        image_cols = list(zip(*image))
        # find the column that have the first ones
        left = self.find_start(0, m, image_cols)

        # find the column that have the first ones
        right = self.find_end(left, m, image_cols)

        # Find the row that starts to have 1s
        low = self.find_start(0, n, image)

        # Find the last row that has is
        high = self.find_end(low, n, image)
        return (right - left + 1) * (high - low + 1)

    def find_start(self, start, end, nums):
        while start < end and not self.has_it(nums[start], '1'):
            start += 1
        return start

    def find_end(self, start, end, nums):
        while start < end and self.has_it(nums[start], '1'):
            start += 1
        return start -1

    def has_it(self, nums, char):
        for i in range(len(nums)):
            if nums[i] == char:
                return True
        return False
