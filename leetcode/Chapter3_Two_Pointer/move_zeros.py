# https://leetcode.com/problems/move-zeroes
# Runtime: 13 ms, faster than 94.62% of Python3 online submissions for Move Zeroes.
# Memory Usage: 17.7 MB, less than 99.01% of Python3 online submissions for Move Zeroes.
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n < 2:
            return nums if n == 1 else []

        # same direction of pointers to maintain the relative order
        p0, ptr = 0, 1
        while ptr < n:
            # find the first zero index
            while p0 < n and nums[p0] != 0:
                p0 += 1
            
            if ptr <= p0:
                ptr = p0 + 1
            
            # find the first non-zero
            while ptr < n and nums[ptr] == 0:
                ptr += 1

            # swap
            if ptr < n:
                nums[ptr], nums[p0] = nums[p0], nums[ptr]

        return nums
