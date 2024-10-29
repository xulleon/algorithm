# https://leetcode.com/problems/first-bad-version/submissions/
# Runtime: 41 ms, faster than 11.71% of Python3 online submissions for First Bad Version.
# Memory Usage: 16.4 MB, less than 95.95% of Python3 online submissions for First Bad Version.
# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        start, end = 1, n
        while start + 1 < end:
            mid = (start + end) // 2
            if not isBadVersion(mid):
                start = mid
            else:
                end = mid
                
        return start if isBadVersion(start) else end
