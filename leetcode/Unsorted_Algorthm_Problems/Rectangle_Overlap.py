# https://leetcode.com/problems/rectangle-overlap/
class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        def isOverlap(rec1, rec2):
            minx1, miny1 = rec1[0], rec1[1]
            maxx1, maxy1 = rec1[2], rec1[3]

            minx2, miny2 = rec2[0], rec2[1]
            maxx2, maxy2 = rec2[2], rec2[3]
            if minx1 == maxx1 or miny1 == maxy1 or minx2 == maxx2 or miny2 == maxy2:
                return False

            if maxx1 <= minx2  or maxx2 <= minx1:
                return False

            if maxy1 <= miny2 or maxy2 <= miny1:
                return False
            return True

        return isOverlap(rec1, rec2)
