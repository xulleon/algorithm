# https://leetcode.com/problems/word-pattern/
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Word Pattern.
# Memory Usage: 16.6 MB, less than 27.27% of Python3 online submissions for Word Pattern.
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        pattern = list(pattern)

        if len(words) != len(pattern):
            return False
        
        word_2_pattern = {}
        pattern_2_word = {}
        for p, w in zip(pattern, words):
            if p not in pattern_2_word:
                pattern_2_word[p] = w
            else:
                if pattern_2_word[p] != w:
                    return False
            if w not in word_2_pattern:
                word_2_pattern[w] = p
            else:
                if word_2_pattern[w] != p:
                    return False
        return True
