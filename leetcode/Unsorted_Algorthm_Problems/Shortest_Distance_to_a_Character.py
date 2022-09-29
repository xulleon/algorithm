# https://leetcode.com/problems/shortest-distance-to-a-character/
class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        def getClosest(target, tindices):
            start, end = 0, len(tindices) - 1
            while start + 1 < end:
                mid = (start + end) // 2
                if tindices[mid] > target:
                    end = mid
                else:
                    start = mid
            return tindices[start] if abs(target - tindices[start]) <= abs(tindices[end] - target) else tindices[end]

        tindices = [ind for ind, v in enumerate(s) if v == c]
        s = list(s)
        n = len(s)
        res = []
        for i in range(n):
            if s[i] == c:
                s[i] = 0
            else:
                s[i] = abs(i - getClosest(i, tindices))

        return s
