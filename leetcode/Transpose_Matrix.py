# https://leetcode.com/problems/transpose-matrix/
class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        res = [[0] * n for _ in range(m)]
        for i in range(n):
            row = 0
            for num in matrix[i]:
                res[row][i] = num
                row += 1

        return res
