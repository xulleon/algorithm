# https://leetcode.com/problems/remove-vowels-from-a-string/
class Solution:
    def removeVowels(self, s: str) -> str:
        s = list(s)
        for i in range(len(s) - 1, -1, -1):
            if s[i] in ['a', 'e', 'i', 'o', 'u']:
                s.pop(i)

        return ''.join(s)
