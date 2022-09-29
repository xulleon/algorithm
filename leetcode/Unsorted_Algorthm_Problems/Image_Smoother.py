# https://leetcode.com/problems/image-smoother/
xys = [(-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0)]
class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        n, m = len(M), len(M[0])
        res = [[0] * m for _ in range(n)]
        for cx in range(n):
            for cy in range(m):
                res[cx][cy] += M[cx][cy]
                count = 1
                for dx, dy in xys:
                    x, y = cx + dx, cy + dy
                    if 0 <= x < n and 0 <= y < m:
                        res[cx][cy] += M[x][y]
                        count += 1

                res[cx][cy] //= count

        return res
