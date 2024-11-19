# https://leetcode.com/problems/combinations/submissions/
# Runtime: 586 ms, faster than 51.92% of Python3 online submissions for Combinations.
"""
This is a typical DFS template. All others variants are based on it with different conditions. I.e. combinations based on a dictionary….
"""
# Solution 1
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        results = []
        self.dfs(n, k, 1, [], results)
        return results

    def dfs(self, n, k, ind, subsets, results):
        if len(subsets) == k:
            results.append(subsets)
            return

        for i in range(ind, n+1):
            subsets.append(i)
            self.dfs(n, k, i + 1, subsets[:], results)
            subsets.pop()

# Solution 2
# Runtime: 195 ms, faster than 19.33% of Python3 online submissions for Combinations.
# Memory Usage: 58.5 MB, less than 96.70% of Python3 online submissions for Combinations.
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if k > n:
            return []
        
        if n == 0:
            return []
        
        nums = [i for i in range(1, n + 1)]
        results = []
        self.dfs(nums, 0, [], k, results)
        return results
    
    def dfs(self, nums, index, subsets, k, results):
        if len(subsets) == k:
            results.append(subsets)
            
        for i in range(index, len(nums)):
            if len(subsets) + 1 > k:
                return
            
            num = nums[i]
            subsets.append(num)
            self.dfs(nums, i + 1, subsets[:], k, results)
            subsets.pop()
    
