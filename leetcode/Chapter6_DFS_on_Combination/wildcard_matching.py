# https://leetcode.com/problems/wildcard-matching/
# https://www.youtube.com/watch?v=3ZDZ-N0EPV0
# Runtime: 222 ms, faster than 79.63% of Python3 online submissions for Wildcard Matching.
# Memory Usage: 26.1 MB, less than 35.15% of Python3 online submissions for Wildcard Matching.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        tmp = []
        # remove multiple *, i.e. '****', case
        first_start = True
        for i in range(len(p)):
            if p[i] == '*':
                if first_start:
                    tmp.append(p[i])
                    first_start = False
            else:
                tmp.append(p[i])
                first_start = True
                
        s = [''] + list(s)
        p = [''] + tmp
        n, m = len(s), len(p)
        # Deal with special case
        if s == '' and (p == '' or p == '*'):
            return True
        
        dp = [[False] * m for _ in range(n)]
        # intialize dp
        dp[0][0] = True
        if m > 1 and p[1] == '*':
            dp[0][1] = True

        for i in range(1, n):
            for j in range(1, m):
                if s[i] == p[j] or p[j] == '?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j] = False

        return dp[n-1][m-1]
