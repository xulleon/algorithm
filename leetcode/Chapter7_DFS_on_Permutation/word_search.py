# https://leetcode.com/problems/word-search
# Runtime: 6909 ms, faster than 9.11% of Python3 online submissions for Word Search.
# Memory Usage: 16.7 MB, less than 32.17% of Python3 online submissions for Word Search.
from collections import defaultdict, deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        max_rows, max_cols = len(board), len(board[0])
        if len(word) == 0:
            return True
        
        if max_rows == 0 or max_cols == 0:
            return False
        
        if max_rows * max_cols < len(word):
            return False
            
        xys = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for x in range(max_rows):
            for y in range(max_cols):
                try:
                    if board[x][y] != word[0]:
                        continue
                except:
                    print(x, y)
                    
                outputs = [board[x][y]]  
                visited = [[False] * max_cols for _ in range(max_rows)]
                visited[x][y] = True
                ret = self.dfs(board, x, y, xys, word, [board[x][y]], visited, outputs)
                if ret == True:
                    return True
        return False
    
    def dfs(self, board, x, y, xys, word, subsets, visited, output):
        rows, cols = len(board), len(board[0])
        if len(word) == len(subsets):
            # print('subsets:', subsets)
            if word == ''.join(subsets):
                # print('got you')
                return True
            return False
        
        for dx, dy in xys:
            cx, cy = x + dx, y + dy
            if not self.valid(cx, cy, rows, cols):
                continue
                
            if visited[cx][cy]:
                continue
                
            subsets.append(board[cx][cy])
            if not word.startswith(''.join(subsets)):
                subsets.pop()
                continue
            visited[cx][cy] = True
            if self.dfs(board, cx, cy, xys, word, subsets[:], visited, output):
                return True
            subsets.pop()
            visited[cx][cy] = False
            
    def valid(self, x, y, max_rows, max_cols):
        return 0 <= x < max_rows and 0 <= y < max_cols

# Solution 2
# 3892 ms Beats 65.71%, 17.71 MB Beats 28.67%

class Solution:
    xys = [(0,1), (1,0), (0,-1), (-1,0)]
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        if rows == 0 and cols == 0:
            return False if len(word) == 0 else False
        
        for i in range(rows):
            for j in range(cols):
                if self.dfs(i, j, board, word):
                    return True
        return False

    def dfs(self, x, y, board, word):
        if board[x][y] != word[0]:
            return False

        # This is the exit!!!
        if len(word) == 1:
            return True

        rows, cols = len(board), len(board[0])
        char = board[x][y]
        
        # Instead using visited, below is a better way to deal the visited problem!!!
        board[x][y] = '#'
        for dx, dy in self.xys:
            xx, yy = x + dx, y + dy

            if 0 <= xx < rows and 0 <= yy < cols and board[xx][yy] != '#':
                if self.dfs(xx, yy, board, word[1:]):
                    return True
        board[x][y] = char

        return False
