# https://leetcode.com/problems/combinations/submissions/
# Runtime: 586 ms, faster than 51.92% of Python3 online submissions for Combinations.
"""
This is a typical DFS template. All others variants are based on it with different conditions. I.e. combinations based on a dictionary….
"""
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
