# https://leetcode.com/problems/palindrome-partitioning/
# Runtime: 63 ms, faster than 17.21% of Python3 online submissions for Palindrome Partitioning.
# Memory Usage: 31.8 MB, less than 89.13% of Python3 online submissions for Palindrome Partitioning.
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        if s == '':
            return []
        if len(s) == 1:
              return [[s]]
        
        results = []
        self.dfs(s, [], results)
        return results
    
    def dfs(self, s, subsets, results):
        if s == '':
            results.append(subsets)

        # by using range(len(s)), you do not need a return when s == ‘’ 
        # because when len(s) is zero, it will not enter the for block, 
        # therefore, end this specific recursive call!!! Otherwise, a return is needed
        for i in range(len(s)):
            chars = s[: i+1]
            if not self.isPalindrome(chars):
                continue
        
            subsets.append(chars)
            self.dfs(s[i+1:], subsets[:], results)
            subsets.pop()
            
    def isPalindrome(self, chars):
        return chars == chars[::-1]
                                                                     
