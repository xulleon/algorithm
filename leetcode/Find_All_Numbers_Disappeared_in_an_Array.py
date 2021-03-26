# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
# Solution One: use dictionary
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        dp = {k: 0 for k in range(1, n + 1)}
        nums = set(nums)
        for item in nums:
            del dp[item]

        return dp

# Solution Two: using set difference
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums = set(nums)
        numset = {k for k in range(1, n + 1)}
        return numset.difference(nums)
