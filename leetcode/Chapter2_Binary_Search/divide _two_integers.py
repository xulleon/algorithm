# https://www.lintcode.com/problem/414/
# 81 ms time cost· 5.06 MB memory cost· Your submission beats 97.20 % Submissions
# take 10/3 for example. instead of using division, we can use subtraction. 
# 1) 10 -3 -3 -3 = 10 - 3 x 3 = 1. when the remaining 1 <= 3, then we can say that the quotient is 3
# 2) we can do it the other way. dividend = 10, divisor = 3, multiplier = 1, quotient = 0
#   2.1) divisor = 3.  if multiplier = 1. we can do multiplier <<= 1. this results multiplier to be 2. divisor <<= 1. this results divisor to be 6. The dividend is 10 - 3x2 = 4
#   2.2) quotient += multiplier, quotient is 2
#   2.3) dividend = 10 - 6 -> 4, divisor = 3, multiplier = 1
#   2.4) dividend > divisor (4 > 3). but dividend < divisor << 1, quotient += multiplier, therefore, quotient is 2 + 1 -> 3
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
