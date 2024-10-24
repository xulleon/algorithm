#
#
from collections import defaultdict
from typing import (
    List,
)

class Solution:
    """
    @param numbers: Give an array numbers of n integer
    @return: Find all unique triplets in the array which gives the sum of zero.
             we will sort your return value in output
    """
    def three_sum(self, numbers: List[int]) -> List[List[int]]:
        # write your code here
        n = len(numbers) 
        if n < 3:
            return []
        numbers = sorted(numbers)
        res = []
        i = 0
        while i <= n - 1:
            target = -numbers[i]
            grps = self.two_sum(numbers, i + 1, n - 1, target)
            for grp in grps:
                grp = [numbers[i]] + grp
                if grp not in res:
                    res.append(grp)
            i += 1
            while i < n - 2 and numbers[i] == numbers[i - 1]:
                i += 1

        return res

    def two_sum(self, nums, start, end, target):
        left, right = start, end
        grps = []
        while left < right:
            if nums[left] + nums[right] == target:
                grps.append([nums[left], nums[right]])
                left += 1
            elif nums[left] + nums[right] < target:
                left += 1
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
            else:
                right -= 1
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

        return grps
