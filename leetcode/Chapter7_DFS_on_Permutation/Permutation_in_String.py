# Permutation in String
# https://leetcode.com/problems/permutation-in-string/
"""
Use sorting. when use dfs, it took too long time and causes Time Limit Exceed error.
"""
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        s1 = ''.join(sorted(s1))

        word_set = set(s1)
        dp = {}
        dif = m - n + 1
        for i in range(dif):

            if s2[i] in dp and not dp[s2[i]]:
                continue

            if s2[i] not in word_set:
                dp[s2[i]] = False

            word = ''.join(sorted(s2[i:i+n]))
            if word in dp:
                continue

            if s1 == word:
                return True
