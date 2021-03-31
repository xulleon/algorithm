# https://leetcode.com/problems/baseball-game/
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        res = []
        for op in ops:
            if op == 'C':
                res.pop()
            elif op == 'D':
                res.append(res[-1] * 2)
            elif op == '+':
                res.append(res[-1] + res[-2])
            else:
                res.append(int(op))
        return sum(res)
