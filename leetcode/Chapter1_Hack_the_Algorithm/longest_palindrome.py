# https://leetcode.com/problems/longest-palindrome/
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Longest Palindrome.
# Memory Usage: 16.7 MB, less than 38.96% of Python3 online submissions for Longest Palindrome.
from collections import defaultdict
class Solution:
    def longestPalindrome(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        # count the number of occurances for each char
        char_len = defaultdict(int)
        for char in s:
            char_len[char] += 1
            
        # retrieve the list of occurences and sort the list 
        # as Ascending regardless which char it is
        len_list = sorted(char_len.values(), reverse = True)
        cnt = 0
        odd_taken = False
        for num in len_list:
            odd = True if num % 2 == 1 else False
            if odd_taken == False and odd:
                # only take the longest odd number as itself is a palidrome
                odd_taken = True
                cnt += num
                continue
                
            # since we already have one odd number, we can only take even number
            if odd:
                cnt += num - 1
            else:
                cnt += num
                
        return cnt
