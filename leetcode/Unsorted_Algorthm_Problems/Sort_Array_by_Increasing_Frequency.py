# https://leetcode.com/problems/sort-array-by-increasing-frequency/
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        from collections import Counter
        dp = Counter(nums)
        nums.sort(key=lambda x: (dp[x], -x))
        return nums
