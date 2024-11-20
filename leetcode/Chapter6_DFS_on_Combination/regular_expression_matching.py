# https://leetcode.com/problems/regular-expression-matching/submissions/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0
        if len(s) == 0:
            return self.checkempty(p)

        if len(p) == 0:
            return False

        f1, p1 = s[0], p[0]
        if len(p) > 1:
            p2 = p[1]
        else:
            p2 = None

        if p2 and p2 == '*':
            if self.compare(f1, p1):
                return (self.isMatch(s[1:], p) or self.isMatch(s, p[2:]))
            else:
                return self.isMatch(s, p[2:])
        else:
            if self.compare(f1, p1):
                return self.isMatch(s[1:], p[1:])

            else:
                return False
        return True

    def checkempty(self, p):

        if len(p) >= 2:
            if p[1] == '*':
                return self.checkempty(p[2:])
        elif len(p) == 0:
            return True

        else: # len(p) == 1:
            return False


    def compare(self, f1, p1):
        if p1 =='.' or f1 == p1:
            return True

        return False

# Dynamic Program
# https://www.youtube.com/watch?v=l3hda49XcDE&t=2s
# Runtime: 7 ms, faster than 69.74% of Python3 online submissions for Regular Expression Matching.
# Memory Usage: 16.7 MB, less than 65.68% of Python3 online submissions for Regular Expression Matching.
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = [''] + list(s)
        p = [''] + list(p)
        
        n, m = len(s), len(p)
        dp = [[False] * m for _ in range(n)]
        dp[0][0] = True
        
        for j in range(1, m):
            if p[j] == '*':
                dp[0][j] = dp[0][j - 2]

        for i in range(1, n):
            for j in range(1, m):
                if s[i] == p[j] or p[j] == '.':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    dp[i][j] = dp[i][j-2]
                    if s[i] == p[j-1] or p[j-1] == '.':
                        dp[i][j] = dp[i][j] or dp[i-1][j]
                else:
                    dp[i][j] = False
                    
        return dp[n-1][m-1]
