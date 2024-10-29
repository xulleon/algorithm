# https://www.lintcode.com/problem/140/description
# 66 ms time cost· 5.00 MB memory cost· Your submission beats 72.60 % Submissions
class Solution:
    """
    @param a: A 32bit integer
    @param b: A 32bit integer
    @param n: A 32bit integer
    @return: An integer
    """
    def fast_power(self, a: int, b: int, n: int) -> int:
        # write your code here
        if a == 0:
            return 0
        if b == 1:
            return 0
            
        if n == 0:
            return 1

        half = self.fast_power(a, b, n//2) % b
        half = (half * half) % b
        if n % 2 == 1:
            half = (half * a) % b

        return half
