# https://leetcode.com/problems/greatest-common-divisor-of-strings/
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        '''
        if the less length one can be the greater length one,
        that means it is the max dividor. by incorsive call,
        to ensure the max divicor be found.
        '''
        if not str1: return str2
        if not str2: return str1
        str1, str2 = (str1, str2) if len(str1) <= len(str2) else (str2, str1)
        if str2.startswith(str1):
            return self.gcdOfStrings(str1, str2[len(str1):])
        return ''

