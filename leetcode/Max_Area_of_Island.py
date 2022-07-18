# https://leetcode.com/problems/max-area-of-island/
xys = [(0,1),(1,0),(0,-1),(-1,0)]
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        self.maxcount = 0
        for x in range(n):
            for y in range(m):
                if visited[x][y]:
                    continue
                visited[x][y] = True
                if grid[x][y] == 1:
                    count = self.helper(grid, x, y, visited)
                    self.maxcount = max(self.maxcount, count)

        return self.maxcount

    def helper(self, grid, xx, yy, visited):
        n, m = len(grid), len(grid[0])
        queue = [(xx,yy)]
        count = 1
        while queue:
            cx, cy = queue.pop(0)
            for dx, dy in xys:
                x, y = cx + dx, cy + dy
                if not (0 <= x < n and 0 <= y < m):
                    continue
                if visited[x][y]:
                    continue

                if grid[x][y] == 0:
                    visited[x][y] = True
                    continue
                queue.append((x, y))
                visited[x][y] = True
                count += 1

        return count
