# https://leetcode.com/problems/wildcard-matching/
# https://www.youtube.com/watch?v=3ZDZ-N0EPV0
# Runtime: 274 ms, faster than 69.37% of Python3 online submissions for Wildcard Matching.
# Memory Usage: 25.1 MB, less than 44.26% of Python3 online submissions for Wildcard Matching.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n, m = len(s), len(p)
        pattern = []
        # process p. a****b - a*b
        si = 0
        first_start = False
        while si < m:
            if p[si] == '*':
                if not first_start:
                    
                    pattern.append(p[si])
                    first_start = True
            else:
                pattern.append(p[si])
                first_start = False
            si += 1
            
        s = [''] + list(s)
        pattern = [''] + pattern
        n, m = len(s), len(pattern)
        dp = [[False] * (m) for _ in range(n)]
        
        dp[0][0] = True
        if m > 1 and pattern[1] == '*':
            dp[0][1] = True

        for i in range(1, n):
            for j in range(1, m):
                a1=pattern[j]
                a2=s[i]
                if pattern[j] == '?' or s[i] == pattern[j]:
                    # abba vs abb? or abba vs abba, both situations, abb is in both s and p
                    dp[i][j] = dp[i-1][j-1]
                elif pattern[j] == '*':
                    # abba vs abba* or abb vs abb*
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]

        return dp[n-1][m-1]
