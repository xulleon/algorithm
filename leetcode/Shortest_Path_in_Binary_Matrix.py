# https://leetcode.com/problems/shortest-path-in-binary-matrix/
xys = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]
class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1

        count = 1
        n, m = len(grid), len(grid[0])
        if n == 1 and m == 1:
            return count

        visited = [[False] * m for _ in range(n)]
        queue = [(0,0)]
        visited[0][0] = True
        while queue:
            size = len(queue)
            count += 1
            for i in range(size):
                cx, cy = queue.pop(0)

                for dx, dy in xys:
                    x, y = cx + dx, cy + dy
                    if not (0 <= x < n and 0 <= y < m):
                        continue

                    if visited[x][y]:
                        continue

                    if grid[x][y] == 1:
                        continue

                    print(f'{x} {y}: count: {count}')
                    if x == n - 1 and y == m - 1:
                        return count

                    queue.append((x, y))
                    visited[x][y] = True

        return -1
