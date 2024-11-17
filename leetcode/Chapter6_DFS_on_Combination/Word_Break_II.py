# https://leetcode.com/problems/word-break-ii/
class Solution:
    """
    The solution is a very typical dfs combination template. By peeling the original string layer
    by layer. The exist condition is that the string can be peeled exactly.
    """
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        results = []

        self.dfs(s, wordDict, [], results)
        return results

    def dfs(self, s, wordDict, subsets, results):
        if len(s) == 0:
            results.append(' '.join(subsets))
            return

        for i in range(len(s)):
            prefix = s[:i+1]
            if prefix not in wordDict:
                continue

            subsets.append(prefix)
            self.dfs(s[len(prefix):], wordDict, subsets[:], results)
            subsets.pop()

# Solution 2: a standard DFS template solution.
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Word Break II.
# Memory Usage: 16.5 MB, less than 95.48% of Python3 online submissions for Word Break II.
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if str == '':
            return []
        
        dp = defaultdict(bool)
        results = []
        self.dfs(s, 0, [], wordDict, dp, results)

        return results
    
    def dfs(self, s, index, subsets, wordDict, dp, results):
        if len(s) == len(''.join(subsets)):
            results.append(' '.join(subsets))
        
        for i in range(index, len(s)):
            prefix = s[index: i + 1]
            
            if prefix not in wordDict:
                continue
                
            # strs = str(prefix) if strs == '' else strs + ' ' + str(prefix)
            subsets.append(prefix)
            items = self.dfs(s, i + 1, subsets[:], wordDict, dp, results)
            subsets.pop()
                                                                     
