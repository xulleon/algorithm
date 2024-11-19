# https://leetcode.com/problems/combination-sum-ii/submissions/
"""
The following is very efficient to resolve problem with the same list of values
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
30
It basically make this problem to be [(1, 100), (2,1)]
"""
# solution 1
# Runtime: 3 ms, faster than 95.03% of Python3 online submissions for Combination Sum II.
# Memory Usage: 16.6 MB, less than 91.87% of Python3 online submissions for Combination Sum II.
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []:
            return []
        
        candidates.sort()
        results = []
        
        self.dfs(candidates, 0, [], target, results)
        return results

    def dfs(self, nums, index, subsets, target, results):
        if target == 0:
            results.append(subsets)
            
        for i in range(index, len(nums)):
            num = nums[i]
            if num > target:
                return
            
            if i != index and nums[i] == nums[i-1]:
                continue
                
            subsets.append(num)
            self.dfs(nums, i + 1, subsets[:], target - num, results)
            subsets.pop()
            
        
# Solution 2

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        from collections import Counter
        counter = Counter(candidates)
        counter = [(k, v) for k, v in counter.items()]
        results = []
        self.dfs(counter, target, [], 0, results)
        return results

    def dfs(self, counter, target, subsets, ind, results):
        if target == 0:
            results.append(subsets)
            return

        if target < 0:
            return

        for i in range(ind, len(counter)):
            candidate, freq = counter[i]
            if freq <= 0:
                continue

            subsets.append(candidate)
            counter[i] = (candidate, freq - 1)
            self.dfs(counter, target - candidate, subsets[:], i, results)
            subsets.pop()
            counter[i] = (candidate, freq)
