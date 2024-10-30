# https://www.lintcode.com/problem/28/record
# 389 ms time cost· 5.75 MB memory cost· Your submission beats 54.60 % Submissions
from typing import (
    List,
)

class Solution:
    """
    if the matrix is flatten, it is a sorted list. Therefore, this problem
    becomes a binary search.
    
    @param matrix: matrix, a list of lists of integers
    @param target: An integer
    @return: a boolean, indicate whether matrix contains target
    """
    def search_matrix(self, matrix: List[List[int]], target: int) -> bool:
        # write your code here
        n, m = len(matrix), len(matrix[0])
        if m == 0 and n == 0:
            return False

        start, end = 0, n * m  - 1
        while start + 1 < end:
            mid = (start + end) // 2
            row, col = mid // m, mid % m
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                end = mid
            else:
                start = mid

        for mid in [start, end]:
            row, col = mid // m, mid % m
            if matrix[row][col] == target:
                return True
        return False
