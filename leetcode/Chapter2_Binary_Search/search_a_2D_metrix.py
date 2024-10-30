# https://www.lintcode.com/problem/38/
# 81 ms time cost· 5.60 MB memory cost· Your submission beats 96.60 % Submissions
"""
We start from the top right corner of the matrix. 
1) when the target was found, it means that
  - there will be no more the target in that row because it is the largest value in that row and it only happened once, therefore, x += 1
  - there will be no more the target in that column because it is the smallest value in that row and it only happened once, therefore, y -= 1
2) if the target is smaller than the conner value, which is smallest in that column, it means there will be no target in that column, hence y -= 1
3) if the target is greater than the conner value, which is greatest in that row, it means there will be no target in that row, hence x += 1
"""
from typing import (
    List,
)

class Solution:
    """
    @param matrix: A list of lists of integers
    @param target: An integer you want to search in matrix
    @return: An integer indicate the total occurrence of target in the given matrix
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> int:
        # write your code here
        n, m = len(matrix), len(matrix[0])
        if n == 0 or m == 0:
            return 0

        if n == 1 and m == 1:
            return 1 if matrix[0][0] == target else 0

        x, y = 0, m - 1
        cnt = 0
        while 0 <= x < n and 0 <= y:
            if matrix[x][y] == target:
                cnt += 1
                x += 1
                y -= 1
            elif matrix[x][y] > target:
                y -= 1
            else:
                x += 1

        return cnt
