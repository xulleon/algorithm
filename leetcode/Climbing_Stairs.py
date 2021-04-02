# https://leetcode.com/problems/climbing-stairs/
class Solution:
    def climbStairs(self, n: int) -> int:
        # basecase condition
        memo = {k: k for k in range(4)}
        return self.climbcase(n, memo)

    def climbcase(self, n, memo):
        if  n in memo:
            return memo[n]

        memo[n] = self.climbcase(n - 1, memo) + self.climbcase(n - 2, memo)
        return memo[n]
