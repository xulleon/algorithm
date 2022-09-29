# https://leetcode.com/problems/remove-outermost-parentheses/
class Solution:
    def removeOuterParentheses(self, S: str) -> str:

        index, n, res = 0, len(S), ''
        while index < n:
            # at this moment, index point to the first "(",
            # which is the outermost parenthes
            pcount = 1
            index += 1
            while index < n and pcount != 0:
                if S[index] == '(':
                    pcount += 1
                else:
                    pcount -= 1

                index += 1
                if pcount == 0:
                    # Found the close parenthes,
                    # which makes the pcount to be 0
                    break
                res += S[index - 1]

        return res
