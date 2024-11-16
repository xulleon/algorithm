# https://leetcode.com/problems/subsets-ii/
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Subsets II.
# Memory Usage: 16.9 MB, less than 12.49% of Python3 online submissions for Subsets II.
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        results = []
        if len(nums) == 0:
            return []
        
        nums.sort()
        self.dfs(nums, 0, [], results)
        return results
    
    def dfs(self, nums, index, subsets, results):
        results.append(subsets)
        
        for i in range(index, len(nums)):
            if i != 0 and nums[i] == nums[i-1] and i > index:
                continue
            subsets.append(nums[i])
            self.dfs(nums, i + 1, subsets[:], results)
            subsets.pop()
