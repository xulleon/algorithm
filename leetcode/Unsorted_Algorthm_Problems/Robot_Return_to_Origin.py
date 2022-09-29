# https://leetcode.com/problems/robot-return-to-origin/
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        from collections import Counter
        mdict = Counter(moves)
        print(mdict)
        dp = {'L': 'R', 'R': 'L', 'U':'D', 'D':'U'}
        for move in mdict:
            if dp[move] not in mdict:
                return False
            if mdict[move] != mdict[dp[move]]:
                return False
        return True
