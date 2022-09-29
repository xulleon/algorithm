# https://leetcode.com/problems/running-sum-of-1d-array/
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        pre, n = 0, len(nums)
        for i in range(n):
            nums[i] += pre
            pre = nums[i]

        return nums
