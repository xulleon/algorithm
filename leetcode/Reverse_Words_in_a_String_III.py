# https://leetcode.com/problems/reverse-words-in-a-string-iii/
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([k[::-1] for k in s.split()])
