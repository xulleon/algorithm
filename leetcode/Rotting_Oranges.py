# https://leetcode.com/problems/rotting-oranges/
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count, n, m = 0, len(grid), len(grid[0])
        visited = [[False] * m for _ in range(n)]
        num_oranges = sum([1 for i in range(n) for j in range(m) if grid[i][j] != 0])
        source = [(i,j) for i in range(n) for j in range(m) if grid[i][j] == 2]
        for i, j in source:
            visited[i][j] = True

        while source:
            size = len(source)
            count += 1
            for _ in range(size):
                cx, cy = source.pop(0)
                for dx, dy in xys:
                    x, y = cx + dx, cy + dy
                    if not (0 <= x < n and 0 <= y < m):
                        continue
                    if visited[x][y]:
                        continue
                    if grid[x][y] == 0:
                        continue

                    source.append((x, y))
                    visited[x][y] = True

        if num_oranges == sum(map(sum, visited)):
            return count - 1 if num_oranges != 0 else 0
        else:
            return -1

