# https://leetcode.com/problems/rotate-string/
class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        if A == '' and B == '':
            return True

        if len(A) != len(B):
            return False

        if set(A) != set(B):
            return False

        right = end = len(A) -1
        while right > 0:
            while A[0] != B[right]:
                right -= 1
            # Found one charactor in B from back equals to first char of A
            delta = end - right
            if A[0: delta + 1] == B[right:] and A[delta + 1:] == B[0: right]:
                return True

            right -= 1

        return False
