# https://leetcode.com/problems/backspace-string-compare/
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def helper(S):
            res = []
            for char in S:
                if char != '#':
                    res.append(char)
                else:
                    if len(res) > 0:
                        res.pop()
            return ''.join(res)

        return helper(S) == helper(T)
