# https://leetcode.com/problems/word-search/solution/
"""
This is a DFS problem. Instead looking combinations from 0 to n-1, it looks for combinations by up, right, down, and right. others will be exactly the same
"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dxy = [(-1, 0), (0, 1, ), (1, 0), (0, -1)]
        self.num_rows = len(board)
        self.num_cols = len(board[0])
        for i in range(self.num_rows):
            for j in range(self.num_cols):
                if not word.startswith(board[i][j]):
                    continue
                visited = [[False for _ in range(self.num_cols)] for _ in range(self.num_rows)]
                visited[i][j] = True
                if self.dfs(board, i, j, dxy, word, [board[i][j]], visited):
                    return True

        return False

    def dfs(self, board, x, y, dxy, word, subsets, visited):
        if ''.join(subsets) == word:
            print(f'word: {word}')
            return True

        for dx, dy in dxy:
            # look for combinations by up, left, down, right
            xx, yy = x + dx, y + dy
            # criteria one to eliminate invalid cells
            if not self.valid_point(xx, yy, self.num_rows, self.num_cols):
                continue

            substr = ''.join(subsets) + board[xx][yy]

            # criteria two to eliminate invalid cells
            if visited[xx][yy] or not word.startswith(substr):
                continue

            # Below is the typical DFS(backtracking)
            subsets.append(board[xx][yy])
            visited[xx][yy] = True
            # This will stop when a solution is found, otherwise, continue looking
            if self.dfs(board, xx, yy, dxy, word[1:], subsets[1:][:], visited):
                return True
            subsets.pop()
            visited[xx][yy] = False

    def valid_point(self, x, y, num_rows, num_cols):
        return 0 <= x < num_rows and 0 <= y < num_cols
