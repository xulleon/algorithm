# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        dp = Counter(nums)
        n = len(nums)
        half = n / 2
        for k in dp:
            if dp[k] > half:
                return k
