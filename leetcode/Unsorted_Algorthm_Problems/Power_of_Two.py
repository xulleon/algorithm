# https://leetcode.com/problems/power-of-two/
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        while n > 1:
            if (n >> 1) << 1 != n:
                return False
            n = n >> 1

        return True
