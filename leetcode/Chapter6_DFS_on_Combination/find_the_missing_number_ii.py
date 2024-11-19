# https://www.lintcode.com/problem/570
from collections import defaultdict
class Solution:
    """
    @param n: An integer
    @param s: a string with number from 1-n in random order and miss one number
    @return: An integer
    """
    def find_missing2(self, n: int, s: str) -> int:
        # write your code hereif n 
        results = []
        self.dfs(s, [], n, results)
      # Easy way to find the missing nuber
        return n * (n + 1) // 2 - sum(results[0])

    def dfs(self, s, subsets, n, results):
        found = False
        if s == '':
            if len(subsets) == n - 1:
                results.append(sorted(subsets))
                found = True
            return 
        if found:
            return 

        for i in range(2):
            if i > len(s):
                break

            prefix = int(s[: i + 1])
            if prefix <= n and prefix not in subsets:
                subsets.append(prefix)
                self.dfs(s[i+1:], subsets[:], n, results)
                subsets.pop()
