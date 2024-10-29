# https://leetcode.com/problems/powx-n/
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Pow(x, n).
# Memory Usage: 16.6 MB, less than 31.41% of Python3 online submissions for Pow(x, n).
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        
        if n < 0:
            x = 1/x
            n = -n
        
        val = self.myPow(x, n // 2)
        val *= val
        if n % 2 == 1:
            val *= x
        return val
