# https://leetcode.com/problems/valid-palindrome-ii/submissions/
# Runtime: 63 ms, faster than 88.55% of Python3 online submissions for Valid Palindrome II.
# Memory Usage: 17 MB, less than 74.94% of Python3 online submissions for Valid Palindrome II.
class Solution:
    def validPalindrome(self, s: str) -> bool:
        n = len(s)
        if n < 2:
            return True
        
        return self.helper(s, 0, n - 1, 0)
        
    def helper(self, s, start, end, cnt):
        
        
        left, right = start, end
        while left <= right:
            if s[left] == s[right]:
                left += 1
                right -= 1
                continue
                
            if cnt == 1:
                return False
            return self.helper(s, left + 1, right, cnt + 1) or self.helper(s, left, right - 1, cnt + 1 )
                
        return True
