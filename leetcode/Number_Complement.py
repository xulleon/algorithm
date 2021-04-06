# https://leetcode.com/problems/number-complement/
class Solution:
    # Solution One: xor calculation
    def findComplement(self, num: int) -> int:
        checks, bit = num, 1
        while checks:
            num = num ^ bit
            bit = bit << 1
            checks = checks >> 1

        return num



    # Solution Two: find the mask length, the do the substraction
    def findComplement(self, num: int) -> int:
        ones = len(bin(num)[2:])
        return int('1' * ones, 2) - num
