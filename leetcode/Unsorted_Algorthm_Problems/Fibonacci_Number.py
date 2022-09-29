# https://leetcode.com/problems/fibonacci-number/
from collections import defaultdict
class Solution:
    def fib(self, n: int) -> int:
        dp = defaultdict(int)
        dp[0], dp[1] = 0, 1

        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]
