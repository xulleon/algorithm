# https://leetcode.com/problems/repeated-substring-pattern/
# solution one: Runtime: 252 ms, faster than 14.80%
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        index = 1

        while index < len(s):
            cur = index
            key = s[:cur]
            while s[cur:].startswith(key):
                cur += index
                if cur == len(s):
                    return True

            index += 1
        return False

# solution 2:
class Solution: Runtime: 36 ms, faster than 75.08%
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
