# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        from collections import Counter
        stonedict = Counter(stones)
        res = 0
        for stone in stonedict:
            if stone in jewels:
                res += stonedict[stone]

        return res

