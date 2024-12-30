# https://leetcode.com/problems/word-pattern-ii/
# 0ms Beats 100.00% 17.95MB Beats 7.37%

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        pn, sn = len(pattern), len(s)
        if pn == 0 and sn == 0:
            return True

        if pn == 0 or sn == 0:
            return False

        pattern2word = {}
        str_set = set()
        pattern = list(pattern)
        return True if self.dfs(pattern, s, pattern2word, str_set) else False
        # a1 = self.dfs(pattern, s, pattern2word, str_set)
        # print(pattern)
        # print(s)
        # print(pattern2word)
        # print(str_set)
        # return a1

    def dfs(self, pattern, s, pattern2word, str_set):
        pn, sn = len(pattern), len(s)
        if pn == 0 and sn == 0:
            return True
        if pn == 0 or sn == 0:
            return False

        key = pattern[0]
        # check if the pattern has been represented or known
        if key in pattern2word:
            substr = pattern2word[key]
            if s.startswith(substr):
                if self.dfs(pattern[1:], s[len(substr):], pattern2word.copy(), str_set.copy()):
                    return True
            return False

        # goes to unkown world
        for i in range(sn):
            key = pattern[0]
            substr = s[:i+1]
            # check if substr has already been represented by another key. 
            # This prevents the different keys represent the same value
            # pattern = 'ab', s = 'aa'. preventing both 'a' and 'b' represent 
            # the same value of 'a'
            if substr in str_set:
                # continue instead of return False.
                # pattern = 'aba', s = 'aaaa'
                continue

            pattern2word[key] = substr
            str_set.add(substr)
            if self.dfs(pattern[1:], s[len(substr):], pattern2word.copy(), str_set.copy()):
                return True
            # else:
            #     return False
            del pattern2word[key]
            str_set.remove(substr)

# Solution 2:
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        if len(s) == 0 and len(pattern) == 0:
            return True
        
        if len(s) == 0:
            return False
        
        if len(pattern) == 0:
            return False
        # s = list(s)
        pattern = list(pattern)
        word2pattern = {}
        p_set = set()
        outputs = []
        return self.dfs(pattern, s, word2pattern, p_set)
    
    def dfs(self, pattern, s, word2pattern, p_set):
        if len(pattern) == 0:
            return len(pattern) == len(s)
        
        key = pattern[0]
        if key in word2pattern:
            substr = word2pattern[key]
            if not s.startswith(substr):
                return False
            
            return self.dfs(pattern[1:], s[len(substr):], word2pattern.copy(), p_set.copy())
        
        for i in range(len(s)):
            key = pattern[0]

            # This ensures that no further DFS is done on the phrase. Therefore,
            # for pattern is 'ab', s is 'aa'. this line prevent both 'a'-> 'a' and 'b'-> 'a'
            if s[:i+1] in p_set:
                continue

            word2pattern[key] = s[:i+1]
            p_set.add(word2pattern[key])
            n = len(word2pattern[key])
            if self.dfs(pattern[1:], s[n:], word2pattern.copy(), p_set.copy()):
                return True
            
            p_set.remove(word2pattern[key])
            del word2pattern[key]
            
        return False
