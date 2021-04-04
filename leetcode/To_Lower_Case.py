# https://leetcode.com/problems/to-lower-case/
class Solution:
    def toLowerCase(self, str: str) -> str:
        res = ''
        lbase = ord('a')
        ubase = ord('A')
        for char in str:
            if 'A' <= char <= 'Z':
                res += chr(lbase + ord(char) - ubase)
            else:
                res += char
        return res
