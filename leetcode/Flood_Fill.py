# https://leetcode.com/problems/flood-fill/
# This is a typical BSF, from one point to surrounded points
xys = [(0,1), (1,0), (0,-1), (-1,0)]
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        def isValid(x, y, rows, cols):
            return 0 <= x < rows and 0 <= y < cols

        rows, cols = len(image), len(image[0])
        visited = [[False] * cols for _ in range(rows)]
        org_val = image[sr][sc]

        queue = [(sr, sc)]
        image[sr][sc] = newColor
        visited[sr][sc] = True
        while queue:
            cx, cy = queue.pop(0)
            for dx, dy in xys:
                x, y = cx + dx, cy + dy
                if not isValid(x, y, rows, cols):
                    continue
                if visited[x][y]:
                    continue

                if image[x][y] != org_val:
                    continue

                queue.append((x,y))
                visited[x][y] = True
                image[x][y] = newColor

        return image
