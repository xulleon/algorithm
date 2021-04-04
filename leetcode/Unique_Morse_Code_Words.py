# https://leetcode.com/problems/unique-morse-code-words/submissions/
morses = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        ord_a, ord_z = ord('a'), ord('z')
        morsedict = {chr(i): k for i, k in zip(range(ord_a, ord_z + 1), morses)}
        res = set()
        for word in words:
            tmp = ''
            for char in word:
                tmp += morsedict[char]
            res.add(tmp)
        return len(res)
