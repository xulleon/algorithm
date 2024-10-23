# https://www.lintcode.com/problem/143/record
#
from typing import (
    List,
)

class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
    def sort_colors2(self, colors: List[int], k: int):
        # write your code here
        n = len(colors)
        if n < 2:
            return [] if n == 0 else colors

        self.quicksort(colors, 0, n - 1)
        return colors

    def quicksort(self, colors, start, end):
        if start >= end:
            return

        left, right = start, end
        pivot = colors[(start + end) // 2]
        while left <= right:
            while left <= right and colors[left] < pivot:
                left += 1

            while left <= right and colors[right] > pivot:
                right -= 1

            if left <= right:
                colors[left], colors[right] = colors[right], colors[left]
                left += 1
                right -= 1

        self.quicksort(colors, start, right)
        self.quicksort(colors, left, end)
