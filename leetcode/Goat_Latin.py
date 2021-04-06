# https://leetcode.com/problems/goat-latin/
vowels = ['a', 'e', 'i', 'o', 'u']
class Solution:
    def toGoatLatin(self, S: str) -> str:
        S = S.split()
        n = len(S)
        for i in range(n):
            if S[i][0].lower() not in vowels:
                S[i] = S[i][1:] + S[i][0]
            S[i] += 'ma' + 'a' * (i + 1)

        return ' '.join(S)
