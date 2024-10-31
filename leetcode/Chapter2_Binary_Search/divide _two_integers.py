# https://www.lintcode.com/problem/414/
# 81 ms time cost· 5.06 MB memory cost· Your submission beats 97.20 % Submissions
class Solution:
    """
    @param dividend: the dividend
    @param divisor: the divisor
    @return: the result
    """
    def divide(self, dividend: int, divisor: int) -> int:
        # write your code here
        max_int, min_int = 2**31 - 1, -2**31
        # deal a special case
        if dividend == min_int and divisor == -1:
            return max_int
        # find the sign of the result
        negative = (dividend < 0) != (divisor < 0)
        # work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)

        #Initialize quotient
        quotient = 0
        while dividend >= divisor:
            tmp_divisor, multiplier = divisor, 1
            while dividend >= (tmp_divisor << 1):
                tmp_divisor <<= 1
                multiplier <<= 1

            # update both dividend and quotient
            dividend -= tmp_divisor
            quotient += multiplier

        if negative:
            quotient = -quotient

        # Ensure that the result is with 32-bit integer range
        return max((min_int), min(max_int, quotient))
