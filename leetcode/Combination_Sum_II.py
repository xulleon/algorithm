# https://leetcode.com/problems/combination-sum-ii/submissions/
"""
The following is very efficient to resolve problem with the same list of values
[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
30
It basically make this problem to be [(1, 100), (2,1)]
"""

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
