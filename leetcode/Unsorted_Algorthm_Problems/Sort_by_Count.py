# https://leetcode.com/problems/reorganize-string/solution/
# Solution One: Runtime: 72 ms, faster than 5.54%
class Solution:
    def reorganizeString(self, S: str) -> str:
        S = list(S)
        res = [S.pop(0)]
        while len(S) > 0:
            if S[0] != res[-1]:
                res.append(S.pop(0))
            else:
                if self.insertion(res, S[0]):
                    S.pop(0)
                else:
                    found = False
                    for i in range(1, len(S)):
                        if i < len(S) and S[0] != S[i]:
                            res.append(S.pop(i))
                            found = True
                            break
                    if not found:
                        return ''
        return ''.join(res)

    def insertion(self, res, char):
        n = len(res)
        index = n - 2
        while index >= 0:
            if res[index] != char:
                if index == 0 or char != res[index - 1]:
                    res = res.insert(index, char)
                    return True

            index -= 1
        return False

# Solution Two:
from collections import Counter
class Solution:
    def reorganizeString(self, S: str) -> str:
        n = len(S)
        # get dict with key as char and value as occurrances
        dp = Counter(S)
        # sort the keys ascending on occurrances
        char_keys = sorted(dp, key=dp.get)
        if dp[char_keys[-1]] > (n + 1) / 2:
            return ''
        ns = []
        for i in char_keys:
            ns.extend([i] * dp[i])
        ans = [None] * n
        ans[::2], ans[1::2] = ns[n//2:], ns[:n//2]
        return ''.join(ans)
