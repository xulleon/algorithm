# https://leetcode.com/problems/word-pattern/
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        pattern = list(pattern)
        s = s.split()
        if len(pattern) != len(s):
            return False

        dp1, dp2 = {}, {}
        for i in range(len(pattern)):
            if pattern[i] not in dp1 and s[i] not in dp2:
                dp1[pattern[i]] = s[i]
                dp2[s[i]] = pattern[i]
            elif pattern[i] in dp1 and s[i] in dp2:
                if dp1[pattern[i]] == s[i] and dp2[s[i]] == pattern[i]:
                    continue
                else:
                    return False
            else:
                return False

        return True
