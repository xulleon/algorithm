# https://leetcode.com/problems/combination-sum/
# Runtime: 3 ms, faster than 97.93% of Python3 online submissions for Combination Sum.
# Memory Usage: 16.6 MB, less than 73.97% of Python3 online submissions for Combination Sum.
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if len(candidates) == 0:
            return []
        
        results = []
        candidates = sorted(set(candidates))
        self.dfs(candidates, 0, [], target, results)
        return results
    
    def dfs(self, nums, index, subsets, target, results):
        if target == 0:
            results.append(subsets)
            
        for i in range(index, len(nums)):
            num = nums[i]
            if num > target:
                break
                
            subsets.append(num)
            self.dfs(nums, i, subsets[:], target - num, results)
            subsets.pop()
