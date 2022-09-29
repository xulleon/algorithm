# https://leetcode.com/problems/happy-number/
class Solution:
    def isHappy(self, n: int) -> bool:
        from collections import defaultdict

        def calculatenum(num):
            res = 0
            while True:
                cur = num % 10
                res += cur * cur
                num = num //10
                if num == 0:
                    return res

        exists = defaultdict(bool)
        nums = []
        while n != 1:
            if exists[n]:
                # means it got into infinite loop.
                return False

            exists[n] = True
            n = calculatenum(n)

        return True
