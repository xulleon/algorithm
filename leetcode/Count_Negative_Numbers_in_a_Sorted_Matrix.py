# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/
lass Solution:
    # Solution One, better performance
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        rows, cols = len(grid), len(grid[0])
        for i in range(rows-1, -1, -1):
            if grid[i][cols-1] >= 0:
                # From left to right and bottom to up,
                # the right bottom must be the smallest node.
                # if the right most cell of any row is greater
                # and equal to 0, then any row from this raw
                # inclusive will be >= 0.
                break
            for j in range(cols - 1, -1, -1):
                if grid[i][j] >= 0:
                    break
                count += 1

        return count

    # Solution Two
    def countNegatives(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] >= 0:
                    continue
                count += 1
        return count
