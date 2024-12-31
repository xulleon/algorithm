# https://leetcode.com/problems/word-break-ii/
# 0ms Beats 100.00%, 17.80MB Beats 11.27%
# this is a very typical dfs problem of reducing the string length to 0
# it is easier than work break
from collections import defaultdict
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        sn, wn = len(s), len(wordDict)
        if sn == 0:
            return True

        outputs = []
        self.dfs(s, wordDict, [], outputs)
        return outputs

    def dfs(self, s, wordDict, subsets, outputs):
        if s == '':
            outputs.append(' '.join(subsets))
            return

        for i in range(len(s)):
            prefix = s[:i+1]
            if prefix not in wordDict:
                continue

            subsets.append(prefix)
            self.dfs(s[i+1:], wordDict, subsets[:], outputs)
            subsets.pop()
