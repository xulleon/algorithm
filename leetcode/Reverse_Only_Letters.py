# https://leetcode.com/problems/reverse-only-letters/
class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        newstr = list(re.sub('[^a-zA-Z]', '', S))
        S = list(S)
        n = len(S)
        for i in range(n):
            if S[i].isalpha():
                S[i] = newstr.pop()

        return ''.join(S)
