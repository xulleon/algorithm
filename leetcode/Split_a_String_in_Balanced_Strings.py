# https://leetcode.com/problems/split-a-string-in-balanced-strings/
class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # variable labled assume start with R. RLLLLRRRLR
        count, l, r, = 0, 0, 0
        for char in s:
            if char == 'R':
                r += 1
            else:
                l += 1
            if r == l:
                count += 1

        return count
