# https://leetcode.com/problems/word-break-ii/
class Solution:
    """
    The solution is a very typical dfs combination template. By peeling the original string layer
    by layer. The exist condition is that the string can be peeled exactly.
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        results = []

        self.dfs(s, wordDict, [], results)
        return results

    def dfs(self, s, wordDict, subsets, results):
        if len(s) == 0:
            results.append(' '.join(subsets))
            return

        for i in range(len(s)):
            prefix = s[:i+1]
            if prefix not in wordDict:
                continue

            subsets.append(prefix)
            self.dfs(s[len(prefix):], wordDict, subsets[:], results)
            subsets.pop()
