# https://leetcode.com/problems/n-queens/submissions/
class Solution:
    """
    This problem is a dfs permutation. for each valid combination, i.e. [1,3,0,2], the index is the row number and the value is the column umber. it equivalent to
    [(0,1), (1,3), (2,0), (3,2)]
    The condition is the similar to qualindrome or others condition. This condition is any two queen can not be in the same row, column, right or left crossing
     - same row: row == rowindex,
     - same column: col == colindex
     - left crossing: row - rowindex == col - colindex. i.e. (0,0), (1,1)
     - rignt crossing: row - rowindex + col - colindex == 0. i.e. (0,3), (1,2)
    """
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1:
            return ["Q"]

        results = []
        self.dfs(n, 0, [], results)
        return results

    def dfs(self, n, index, subsets, results):
        if len(subsets) == n:
            q_subsets = self.draw(subsets, n)
            results.append(q_subsets)
            return

        for col in range(n):
            if not self.qualified(subsets, col):
                continue

            subsets.append(col)
            self.dfs(n, col, subsets[:], results)
            subsets.pop()


    def qualified(self, subsets, col):
        row = len(subsets)

        for rowindex, colindex in enumerate(subsets):
            if row - rowindex + col - colindex == 0:
                return False

            if row - rowindex == col - colindex:
                return False

            if row == rowindex or col == colindex:
                return False

        return True

    def draw(self, subsets, n):
        res = []
        for q in subsets:
            q_str = ["." if i != q else "Q" for i in range(n) ]
            q_str = ''.join(q_str)
            res.append(q_str)
        return res
