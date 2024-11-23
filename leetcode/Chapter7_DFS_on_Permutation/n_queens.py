# https://leetcode.com/problems/n-queens/submissions/
# Runtime: 1083 ms, faster than 5.01% of Python3 online submissions for N-Queens.
# Memory Usage: 17.3 MB, less than 10.95% of Python3 online submissions for N-Queens.
from collections import defaultdict
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n -1 == 0:
            return [['Q']]
        
        results = []
        visited = defaultdict(bool)
        nums = [i for i in range(n)]
        self.dfs(nums, [], visited, results)
        return results
    
    def dfs(self, nums, subsets, visited, results):
        if len(nums) == len(subsets):
            points = self.translate_to_points(subsets)
            if self.isValid(points):
                graph = self.make_graph(points)
                results.append(graph)
            return
        
        for i in range(len(nums)):
            if nums[i] in visited and visited[i]:
                continue
                
            subsets.append(nums[i])
            visited[i] = True
            self.dfs(nums, subsets[:], visited, results)
            subsets.pop()
            visited[i] = False
            
    def translate_to_points(self, dots):
        points = []
        for row, col in enumerate(dots):
            points.append((row, col))
        return points
            
    def isValid(self, points):
        k = len(points)
        for i in range(k-1):
            row1, col1 = points[i]
            for j in range(i + 1, k):
                row2, col2 = points[j]
                # right cross or left cross
                if row1 - col1 == row2 - col2 or row1 + col1 == row2 + col2:
                    return False
                # Same row or col
                if row1 == row2  or col1 == col2:
                        return False
        return True
                       
    def make_graph(self, points):
        n = len(points)
        rows = []
        for row, col in points:
            rows.append(self.make_row(col, n))
        return rows
            
    def make_row(self, col, n):
        return ''.join(['Q' if i == col else '.' for i in range(n)])
