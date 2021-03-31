# https://leetcode.com/problems/two-sum-less-than-k/
class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right = 0, len(nums) - 1
        mid = (left + right)//2
        maxsum = -1
        while left < right:
            if nums[left] + nums[right] >= k:
                right -= 1
            else:
                maxsum = max(maxsum, nums[left] + nums[right])
                left += 1

        return maxsum
