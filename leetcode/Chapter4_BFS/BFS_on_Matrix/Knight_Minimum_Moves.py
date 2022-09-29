# https://leetcode.com/problems/minimum-knight-moves/
'''
This is a typical BFS problem. only different is how to find its neighbors.
It is another BFS on Matrix with the nieghbor in a knight step.
In order to make it better performance, below uses bidirectional BFS. Even though, it still exceed time limited.
'''
from collections import defaultdict
class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        if x == 0 and y == 0:
            return 0

        xy = [(1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2)]
        org_queue = [(0,0)]
        dest_queue = [(x,y)]
        ocnt = 0
        dcnt = 0
        org_visited = defaultdict(bool)
        dest_visited = defaultdict(bool)
        org_visited[(0,0)] = True
        dest_visited[(x, y)] = True
        while True:
            org_size = len(org_queue)
            dest_size = len(dest_queue)
            for _ in range(org_size):
                oxx, oyy = org_queue.pop(0)

                for odx, ody in xy:
                    ocx, ocy = oxx + odx, oyy + ody
                    if dest_visited[(ocx, ocy)]:
                        print(f'1 - {ocnt}, {dcnt}')
                        return ocnt + dcnt + 1

                    if org_visited[(ocx, ocy)]:
                        #print(f'({cx}, {cy})')
                        continue

                    org_queue.append((ocx, ocy))
                    org_visited[(ocx, ocy)] = True
            ocnt += 1

            for _ in range(dest_size):
                dxx, dyy = dest_queue.pop(0)

                for ddx, ddy in xy:
                    dcx, dcy = dxx + ddx, dyy + ddy
                    if org_visited[(dcx, dcy)]:
                        print(f'2 - {ocnt}, {dcnt}')
                        return ocnt + dcnt + 1

                    if dest_visited[(dcx, dcy)]:
                        #print(f'({cx}, {cy})')
                        continue

                    dest_queue.append((dcx, dcy))
                    dest_visited[(dcx, dcy)] = True
            dcnt += 1

        return ocnt + dcnt
