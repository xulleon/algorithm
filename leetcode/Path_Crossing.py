# https://leetcode.com/problems/path-crossing/
xys = {'N': (0,1), 'S': (0,-1), 'E': (1,0), 'W': (-1,0)}
class Solution:
    def isPathCrossing(self, path: str) -> bool:
        paths = [(0,0)]
        x, y = 0, 0
        for dir in path:
            dx, dy = xys[dir]
            x, y = x+dx, y+dy
            if (x, y) in paths:
                return True
            else:
                paths.append((x,y))

        return False
