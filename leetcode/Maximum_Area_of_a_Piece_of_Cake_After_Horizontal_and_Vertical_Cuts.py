# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        '''
        The answer is not correct. when I reduce the w and h, everything goes well.
        '''
        def findMaxGap(cuts):
            max_gap = 0
            for i in range(1, len(cuts)):
                max_gap = max(cuts[i] - cuts[i-1], max_gap)
            return max_gap

        horizontalCuts.sort()
        verticalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts = [0] + verticalCuts + [w]

        maxHgap = findMaxGap(horizontalCuts) % (10**9 + 7)
        maxVgap = findMaxGap(verticalCuts) % (10**9 + 7)
        return maxHgap * maxVgap % (10**9 + 7)

