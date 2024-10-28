# https://leetcode.com/problems/rotate-string/
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Rotate String.
# Memory Usage: 16.5 MB, less than 35.93% of Python3 online submissions for Rotate String.
from collections import defaultdict
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        if n != len(goal):
            return False
        
        if n == 0:
            return True
        
        for i in range(n):
            if goal[i] == s[0]:
                if s == goal[i:] + goal[:i]:
                    return True
                
        return False
      
