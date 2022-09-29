# https://leetcode.com/problems/number-of-islands/
# Runtime: 397 ms, faster than 76.64% of Python3 online submissions for Number of Islands.
'''
This is a very typical BFS on Matrix problem. Only tricks are
- use for loop to find the first 1 in a island
- use xy to nevigate four neighbors of a point.
- do not forget to use visited to skip already visited point.
'''
from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        xy = [(0, -1),(-1, 0),(0, 1),(1, 0)]
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        cnt = 0
        for x in range(n):
            for y in range(m):
                if grid[x][y] != '1' or visited[x][y]:
                    continue

                self.bfs(grid, x, y, xy, visited)
                cnt += 1
        return cnt

    def bfs(self, grid, x, y, xy, visited):
        n, m = len(grid), len(grid[0])
        queue = deque([(x, y)])
        visited[x][y] = True
        while queue:
            xx, yy = queue.popleft()
            for dx, dy in xy:
                cx, cy = xx + dx, yy + dy
                if 0 <= cx < n and 0 <= cy < m:

                    if grid[cx][cy] != '1' or visited[cx][cy]:
                        continue

                    queue.append((cx, cy))
                    visited[cx][cy] = True
