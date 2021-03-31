# https://leetcode.com/problems/add-digits/
class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            num = sum([int(k) for k in str(num)])
        return num
