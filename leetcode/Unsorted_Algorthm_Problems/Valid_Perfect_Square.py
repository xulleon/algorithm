# https://leetcode.com/problems/valid-perfect-square/
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num < 2:
            return True
        left, right = 2, num//2
        while left <= right:
            x = left + (right - left)//2
            new_num = x * x
            if new_num == num:
                return True
            if new_num > num:
                right = x -1
            else:
                left = x + 1

        return False
