# https://leetcode.com/problems/reverse-string-ii/
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n = len(s)
        if n <= k:
            return s[::-1]

        for start in range(0, n, 2 * k):
            end = start + k if start + k <= n else n
            s = s[0: start] + s[start: end][::-1] + s[end:]
        return s
