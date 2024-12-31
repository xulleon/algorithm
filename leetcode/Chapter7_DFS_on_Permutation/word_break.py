# https://leetcode.com/problems/word-break/
# 3 ms Beats 70.28%, 18.05 MB Beats 8.57%

from collections import defaultdict
class Solution:
    '''
    this is recursive call, which means there are lots of tracking back call of dfs. in the 
    even s = 'aaaaaaaaaaaaab', without DP, lots of repetitive calculation needs to be done,
    which will make "excceding limit time". check out how to use dp in the code below.
    if s in dp:
        return dp[s]
    and 
    if self.dfs(s[i+1:], wordDict, dp):
        dp[s[i+1:]] = True
            return True
    else:
        dp[s[i+1:]] = False

    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        sn, wn = len(s), len(wordDict)
        if sn == 0:
            return True

        dp = defaultdict(bool)
        return self.dfs(s, wordDict, dp) 

    def dfs(self, s, wordDict, dp):
        if s == '':
            print('dp:', dp)
            return True

        if s in dp:
            # This is a DP. with memorizing the result from the result of 
            # self.dfs(s[i+1:], wordDict, dp), the tracing back will be 
            # much faster than redoing all it over again
            return dp[s]
        

        for i in range(len(s)):
            substr = s[:i+1]
            if substr not in wordDict:
                continue

            dp[substr] = True
            if self.dfs(s[i+1:], wordDict, dp):
                # record the pass and failure of the above dfs call
                # it greatly optimized and speeded up the calculation
                dp[s[i+1:]] = True
                return True
            else:
                # there is no "return False" following as it will need 
                # to increase "i" for for loop
                dp[s[i+1:]] = False
        # this is important as it need to remember success or failure of the dfs call.
        return False
