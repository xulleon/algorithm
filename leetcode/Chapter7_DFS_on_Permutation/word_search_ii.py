# https://leetcode.com/problems/word-search-ii/
# solution 1 - trie
# 5261 ms Beats 55.06% 18.67 MB Beats 79.38%
class Solution:
    def findWords(self, board, words):
        # Step 1: Build a Trie from the word list
        def build_trie(words):
            trie = {}
            for word in words:
                node = trie
                for char in word:
                    if char not in node:
                        node[char] = {}
                    node = node[char]
                node['#'] = True  # '#' marks the end of a word
            return trie
        
        # Step 2: Perform DFS to find words
        def dfs(node, x, y, path):
            char = board[x][y]
            if char not in node:
                return
            
            next_node = node[char]
            path += char
            
            # Check if we found a word
            if '#' in next_node:
                result.add(path)
            
            # Mark the cell as visited
            board[x][y] = '#'
            
            # Explore all four directions
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] != '#':
                    dfs(next_node, nx, ny, path)
            
            # Restore the cell
            board[x][y] = char
        
        # Initialization
        trie = build_trie(words)
        result = set()
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        # Start DFS from each cell
        for i in range(m):
            for j in range(n):
                dfs(trie, i, j, "")
        
        return list(result)

  # Solution 2 (Time limit exceeding)
from collections import defaultdict
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        words0 = defaultdict(list)
        for word in words:
            words0[word[0]].append(word)

        xys = [(0,1), (1,0), (0,-1), (-1,0)]
        outputs = []
        # print(words0)
        word_visited = defaultdict(bool)
        xdp = defaultdict(bool)
        for row in range(rows):
            for col in range(cols):
                char = board[row][col]
                if char not in words0:
                    continue

                for word in words0[char]:
                    if word in word_visited and word_visited[word]:
                        continue
                    visited = defaultdict(bool)
                    visited[(row, col)] = True 
                    if self.dfs(row, col, board, word[1:], xys, visited, xdp):
                        word_visited[word] = True
                        outputs.append(word)
        return outputs

    def dfs(self, row, col, board, word, xys, visited, xdp):
        rows, cols = len(board), len(board[0])
        if word == '':
            return True

        for dx, dy in xys:
            x = row + dx
            y = col + dy
            if self.isValid(x, y, rows, cols, xdp):
                if board[x][y] != word[0]:
                    continue

                if visited[(x,y)]:
                    continue
                visited[(x, y)] = True
                if self.dfs(x, y, board, word[1:], xys, visited, xdp):
                    return True
                visited[(x, y)] = False

        return False

    def isValid(self, x, y, rows, cols, xdp):
        if (x, y) in xdp:
            return xdp[(x, y)]
        if 0 <= x < rows and 0 <= y < cols:
            xdp[(x,y)] = True
            return True
        else:
            xdp[(x, y)] = False
            return False


  
