# https://leetcode.com/problems/word-ladder/submissions/
from collections import defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if not beginWord or not endWord or endWord not in wordList or not wordList:
            return 0

        wordList.append(beginWord)
        visited = {beginWord: True}
        indegree = self.find_nbrs(wordList)

        return self.bfs(indegree, beginWord, endWord, visited)


    def bfs(self, indegree, start, end, visited):
        if start == end:
            return 0
        queue = [(start, 1)]
        while queue:
            size = len(queue)
            for _ in range(size):
                word, level = queue.pop(0)
                for i in range(len(word)):
                    new_word = word[0:i] + '*' + word[i+1:]
                    for nbr in indegree[new_word]:
                        if nbr == end:
                            return level + 1
                        if nbr not in visited:
                            queue.append((nbr, level + 1))
                            visited[nbr] = True
                            # remember to empty the list to optimizethe algorithm
                            indegree[new_word] = []

        return 0
    # For graph problems, constructing a word tree, using the following * method
    # is most efficient template. need to remember
    def find_nbrs(self, wordList):
        indegree = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                new_word = word[0: i] + '*' + word[i+1:]
                indegree[new_word].append(word)

        return indegree

