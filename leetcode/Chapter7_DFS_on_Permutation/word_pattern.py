# https://leetcode.com/problems/word-pattern/
# Solution 1: None DFS way
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Word Pattern.
# Memory Usage: 16.6 MB, less than 27.27% of Python3 online submissions for Word Pattern.
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        pattern = list(pattern)

        if len(words) != len(pattern):
            return False
        # using the two dicts to ensure this scenario, pattern = ‘ab’, s = ‘aa’
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

# Solution 2
# 0 ms Beats 100%. 18.65MB Beats 6.64%
class Solution:
    '''
    Using DFS way to resolve this issue. 
    perticularly removing known match until both pattern and s reach to 0 length at the same time.
    '''
    def wordPattern(self, pattern: str, s: str) -> bool:
        sn, pn = len(s), len(pattern)
        if sn == 0 and pn == 0:
            return True

        if sn == 0 or pn == 0:
            return False

        pattern2word = {}
        str_set = set()
        s = s.split(' ')
        pattern = list(pattern)
        return True if self.dfs(pattern, s, pattern2word, str_set) else False

    def dfs(self, pattern, s, pattern2word, str_set):

        pn, sn = len(pattern), len(s)
        if pn == 0 and sn ==0:
            # exactly match in value and length
            return True
        if pn == 0 or sn == 0:
            # partially match only
            return False

        # dynamic programming to deal with known match 
        key = pattern[0]
        if key in pattern2word:
            substr = pattern2word[key]
            if substr != s[0]:
                return False
            if self.dfs(pattern[1:], s[1:], pattern2word.copy(), str_set.copy()):
                return True
            else:
                return False

        # goes to unknown world
        for i in range(pn):
            key = pattern[0]
            substr = s[0]
            if substr in str_set:
                # this word has been represented by other key
                # prevent pattern = 'ab', s = 'aa'. both 'a' and 'b' all represent 'a'
                return False

            # processing it in DFS way
            pattern2word[key] = substr
            str_set.add(substr)
            if self.dfs(pattern[1:], s[1:], pattern2word.copy(), str_set.copy()):
                return True
            else:
                # This is very important!!! to beat 100% submitters
                return False
            del pattern2word[key]
            str_set.remove(substr)
