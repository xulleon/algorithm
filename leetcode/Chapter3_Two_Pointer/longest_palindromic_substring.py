# https://leetcode.com/problems/longest-palindromic-substring/
# SOLUTION 1 - Emeration from center
# Runtime: 220 ms, faster than 90.49% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 16.8 MB, less than 29.30% of Python3 online submissions for Longest Palindromic Substring.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        @param s: input string
        @return: a string as the longest palindromic substring
        """
        # write your code here
        n = len(s)
        if n < 2:
            return '' if n == 0 else s[0]
        longest = 0
        for i in range(n):
            # odd
            dist = self.get_lp(s, i, i)
            if dist > longest:
                longest = dist
                start = i - dist // 2

            # even
            dist = self.get_lp(s, i, i + 1)
            if dist > longest:
                longest = dist
                # it is even condition, count itself, it needs to substract 1
                start = i - (dist // 2 - 1)

        return s[start: start + longest]

    def get_lp(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

# SOLUTION 2 - Dynamic Programming
# Runtime: 2088 ms, faster than 27.77% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 33.2 MB, less than 6.21% of Python3 online submissions for Longest Palindromic Substring.
class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        @param s: input string
        @return: a string as the longest palindromic substring
        """
        # write your code here
        # The theory of dynamic programming is if s[start: end] 
        # is a palindrome then s[start] == s[end] and s[start + 1: end - 1] 
        # must be a palindrome
        n = len(s)
        if n < 2:
            return '' if n == 0 else s[0]
        
        # The row and column represent start and end in a string
        dp = [[0] * n for i in range(n)]
        
        # Initialize the string s[0]=?=s[0], s[1] =?= s[1] ...s[n-1] =?= s[n-1]
        longest = 1
        for i in range(n):
            dp[i][i] = 1
            str_start, str_end = i, i
         
        # Initialize the neighbor string  s[0] =?= s[1] (means , s[1] =?= s[2] ...s[n-2] =?= s[n-1]
        for i in range(n - 1):
            if s[i] == s[i+1]:
                dp[i][i + 1] = 2
                # longest = 2
                str_start, str_end = i, i + 1
        # Since we know if each char and its neighbor combined is a palindrome, 
        # then we will expend each neighbor pair on its left and right
        # the above already initialized 1string of 1 char and 2 chars. next we will test starting from 3 chars
        # The following i is the difference between start and end. i = end - start. 2 
        # means that there are 2+1 = 3 chars. 
        # Here start is represented by row number and end is represented by column number
        for i in range(2, n): 
            # start is the row
            for start in range(n - i): 
                # we already know start, and start + (2 - 1) based on dp above
                end = start + i

                if start < n and end > n:
                    break

                if s[start] == s[end] and dp[start + 1][end - 1]:
                    dp[start][end] = dp[start + 1][end - 1] + 2
                    str_start = start
                    str_end = end
        
        return s[str_start: str_end + 1]
                    
