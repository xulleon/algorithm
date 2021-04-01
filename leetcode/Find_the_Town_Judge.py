# https://leetcode.com/problems/find-the-town-judge/
class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            return 1 if N == 1 else -1

        from collections import defaultdict
        dp = defaultdict(set)
        for grp in trust:
            dp[grp[1]].add(grp[0])

        res = [k for k, v in dp.items() if len(v) == N -1]
        if len(res) != 1:
            return -1

        for v in dp.values():
            if res[0] in v:
                return -1

        return res[0]
