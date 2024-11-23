# Permutation in String
# https://leetcode.com/problems/permutation-in-string/
# Solution 1. find any letter existing in s1 on s2, 
# then get the substring of next len(s1), compare of 
# Counter(s1) == Counter(i: i + len(s1)), if it is true, 
# then one of s1's permutations is in s2
# Runtime: 2553 ms, faster than 10.85% of Python3 online submissions for Permutation in String.
# Memory Usage: 17 MB, less than 9.62% of Python3 online submissions for Permutation in String.
from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_counter = Counter(s1)
        n,m = len(s1), len(s2)
        s2_cnt = 0
        while s2_cnt < m:
            while s2_cnt <m and  s2[s2_cnt] not in s1_counter:
                s2_cnt += 1
                continue
                
            sub_s2 = s2[s2_cnt: s2_cnt + n]
            if s1_counter == Counter(sub_s2):
                return True
            
            s2_cnt += 1
            if s2_cnt >= m:
                return False


# Solution 2
"""
Use sorting. when use dfs, it took too long time and causes Time Limit Exceed error.
"""
from collections import defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False
        s1 = ''.join(sorted(s1))

        word_set = set(s1)
        dp = {}
        dif = m - n + 1
        for i in range(dif):

            if s2[i] in dp and not dp[s2[i]]:
                continue

            if s2[i] not in word_set:
                dp[s2[i]] = False

            word = ''.join(sorted(s2[i:i+n]))
            if word in dp:
                continue

            if s1 == word:
                return True

# Solution 3 - dfs: time limit exceed. need to optimize
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # print(s1, s2)
        if len(s2) == 0:
            return False
        
        if len(s2) == 0:
            return True
        
        if len(s1) > len(s2):
            return False
        
        # s1 = list(s1).sort()
        # print('000-s1:', list(s1))
        results = []
        visited = [False] * len(s1)
        if self.dfs(s1, s2, 0, [], visited, results):
            return True
        
        return False
    
    def dfs(self, s1, s2, index, subsets, visited, results):
        if len(subsets) == len(s1):
            if ''.join(subsets) in s2:
                self.found = True
                return True
            
            results.append(subsets)
            return False

        for i in range(len(s1)):
            if visited[i]:
                continue
                
            if i > 0 and s1[i] == s1[i-1] and visited[i] == False:
                continue
                
            subsets.append(s1[i])
            visited[i] = True
            if self.dfs(s1, s2, i+1, subsets[:], visited, results):
                return True
            visited[i] = False
            subsets.pop()
