# https://leetcode.com/problems/factor-combinations/
class Solution:
    def getFactors(self, n: int) -> List[List[int]]:
        res = []
        self.dfs(n, [], res)
        return res

    def dfs(self, n, subsets, res):
        start = subsets[-1] if subsets else 2
        for i in range(start, int(n**0.5) + 1):
            if n % i == 0:
                subsets.append(i)
                res.append(subsets[:] + [n // i])
                self.dfs(n // i, subsets[:], res)
                subsets.pop()
