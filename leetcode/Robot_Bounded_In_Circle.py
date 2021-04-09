# https://leetcode.com/problems/robot-bounded-in-circle/
xys = [(0,1), (1,0), (0,-1), (-1,0)]
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        # 0 - north, 1 - right, 2 for down, 3 for left
        direction = 0
        x = y = 0
        for opt in instructions:
            if opt == 'R':
                direction = (direction + 1) % 4

            elif opt == 'L':
                direction = (direction + 3) % 4
            else:
                x += xys[direction][0]
                y += xys[direction][1]

        return (x == 0 and y == 0) or direction != 0
