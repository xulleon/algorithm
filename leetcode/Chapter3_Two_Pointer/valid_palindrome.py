# https://leetcode.com/problems/valid-palindrome/submissions/
# Runtime: 7 ms, faster than 98.33% of Python3 online submissions for Valid Palindrome.
# Memory Usage: 17 MB, less than 85.98% of Python3 online submissions for Valid Palindrome.
class Solution:
    def isPalindrome(self, s: str) -> bool:    
        n = len(s)
        if n < 2:
            return True

        s = s.lower()
        left, right = 0, n - 1
        while left < right:
            while left <= right and not s[left].isalnum():
                left += 1
                
            while left < right and not s[right].isalnum():
                right -= 1
                
            if left < right:   
                if s[left] != s[right]:
                    return False
            
            left += 1
            right -= 1
            
        return True
