# https://leetcode.com/problems/array-partition-i/
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        res = 0
        for i in range(0, n, 2):
            res += min(nums[i: i+2])
        return res
