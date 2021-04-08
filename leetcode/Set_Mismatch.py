# https://leetcode.com/problems/set-mismatch/
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums.sort()
        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if len(nums[mid:]) == len(set(nums[mid:])):
                end = mid
            else:
                start = mid

        origset = set([k for k in range(1, len(nums) + 1)])
        missing = origset.difference(set(nums))
        return [nums[start]] + list(missing)
