# https://leetcode.com/problems/find-common-characters/
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        '''
        The idea first count all number of letters for
        each str recorded by a dict. go through all chars
        and find the min numbers of occurances. Only the
        char which common to all strings will eventually
        recorded into thre final result.
        '''
        n = len(A)
        res = []
        from collections import Counter
        dp = {k: Counter(k) for k in A}
        for k in dp[A[0]]:
            found = True
            count = dp[A[0]][k]
            for i in range(1, len(A)):
                if k not in dp[A[i]]:
                    found = False
                    break
                else:
                    count = min(count, dp[A[i]][k])
            if found:
                res.extend([k] * count)
        return res
