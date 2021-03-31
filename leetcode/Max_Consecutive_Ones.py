# https://leetcode.com/problems/max-consecutive-ones/
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxones = 0
        count = nums[0]
        for i in range(1, len(nums)):
            if (nums[i] == 1 and nums[i-1] ==1) or nums[i] == 1:
                count += 1
            else:
                # when it is a zero, record the max ones and reset count
                maxones = max(maxones, count)
                count = 0
        return max(maxones, count)
