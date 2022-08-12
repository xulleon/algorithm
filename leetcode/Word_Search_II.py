# https://leetcode.com/problems/word-search-ii/submissions/

"""
This version can be improved. Some problems have time limit exceeded error.
"""
from copy import deepcopy
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        words = self.validate_words(board, words)
        rows, cols = len(board), len(board[0])
        dxy = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        orig_visited = [[False for _ in range(cols)] for _ in range(rows)]
        results = []
        for i in range(rows):
            for j in range(cols):
                res = []
                word_list = [word for word in words if word.startswith(board[i][j])]
                if not word_list:
                    continue
                visited = deepcopy(orig_visited)
                visited[i][j] = True
                word_list = [word[1:] for word in word_list]
                self.dfs(board, [board[i][j]], i, j, dxy, word_list, visited, res)
                for word in res:
                    if word in words:
                        words.remove(word)
                        results.append(word)
        return results

    def validate_words(self, board, words):
        word_set = set()
        for row in board:
            word_set.update(row)

        return [word for word in words if not set(word).difference(word_set)]


    def dfs(self, board, subsets, cx, cy, dxy, word_list, visited, res):
        for wd in word_list:
            if wd == '':
                a1= len(word_list)
                word_list.remove('')
                a2= len(word_list)
                res.append(''.join(subsets))
                return True

        for dx, dy in dxy:
            x, y = cx + dx, cy + dy
            if not (0 <= x < len(board) and 0 <= y < len(board[0])):
                continue

            if visited[x][y]:
                continue
            new_word_list = [wd for wd in word_list if wd.startswith(board[x][y])]
            if not new_word_list:
                continue

            new_word_list = [wd[1:] for wd in new_word_list]
            visited[x][y] = True
            subsets.append(board[x][y])

            if self.dfs(board, subsets[:], x, y, dxy, new_word_list, visited, res):
                return True
            visited[x][y] = False
            subsets.pop()
