# https://leetcode.com/problems/word-break/
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = defaultdict(bool)
        return self.dfs(s, wordDict, dp)

    def dfs(self, s, wordDict, dp):
        if s in dp and dp[s] == False:
            return False

        if len(s) == 0:
            return True

        for i in range(len(s)):
            prefix = s[:i + 1]

            if prefix not in wordDict:
                continue

            if prefix in dp and dp[s]:
                return self.dfs(s[i+1:], wordDict, dp)

            dp[prefix] = True
            if self.dfs(s[i+1:], wordDict, dp):
            # only need to know if this occurs, not combinations
                return True

        # since it does not collect all possible combinations, use this. Otherwise, can not use it.
        dp[prefix] = False
