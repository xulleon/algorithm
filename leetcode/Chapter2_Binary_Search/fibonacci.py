# https://leetcode.com/problems/fibonacci-number/
# Runtime: 325 ms, faster than 29.30% of Python3 online submissions for Fibonacci Number.
# Memory Usage: 16.6 MB, less than 25.75% of Python3 online submissions for Fibonacci Number.
class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        
        return self.fib(n - 1) + self.fib(n - 2)
