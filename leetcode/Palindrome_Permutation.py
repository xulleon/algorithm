# https://leetcode.com/problems/palindrome-permutation/
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        from collections import Counter
        sdict = Counter(s)
        pal = 0
        for key in sdict:
            pal += sdict[key] % 2
            if pal > 1:
                return False
        return True
