# https://leetcode.com/problems/subsets/
# Solution 1
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Subsets.
# Memory Usage: 16.8 MB, less than 15.63% of Python3 online submissions for Subsets.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []
        
        results = []
        self.dfs(nums, 0, [], results)
        return results
        
    def dfs(self, nums, index, subset, results):
        if index == len(nums):
            results.append(subset)
            return
        
        self.dfs(nums, index + 1, subset[:], results)
        subset.append(nums[index])
        self.dfs(nums, index + 1, subset[:], results)

# Solution 2
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Subsets.
# Memory Usage: 16.7 MB, less than 53.10% of Python3 online submissions for Subsets.
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        results = []
        if len(nums) == 0:
            return results
        
        nums.sort()
        self.dfs(nums, 0, [], results)
        return results
        
    def dfs(self, nums, index, subsets, results):
        results.append(subsets)
        
        for i in range(index, len(nums)):
            subsets.append(nums[i])
            self.dfs(nums, i + 1, subsets[:], results)
            subsets.pop()
