# https://leetcode.com/problems/longest-continuous-increasing-subsequence/
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        index, maxcount = 1, 1
        while index < len(nums):
            count = 1
            while index < len(nums) and nums[index-1] < nums[index]:
                count += 1
                index += 1
            else:
                maxcount = max(maxcount, count)
                index += 1
        return maxcount
