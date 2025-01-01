# https://leetcode.com/problems/word-ladder/
# 55 ms Beats 85.63% 20.83 MB Beats 29.18%

from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord == endWord:
            return 1
        if endWord not in wordList:
            return 0

        wordList.append(endWord)
        graph = self.build_graph(wordList)
        return self.bfs(beginWord, endWord, graph)

    def build_graph(self, wordList):
        graph = defaultdict(list)
        for word in wordList:
            n = len(word)
            for i in range(n):
                graph[word[:i] + '*' + word[i+1:]].append(word)
        return graph

    def bfs(self, beginWord, endWord, graph):
        queue = deque()
        queue.append(beginWord)
        visited = defaultdict(bool)
        visited[beginWord] = True
        cnt = 0
        while queue:
            size = len(queue)
            cnt += 1
            for i in range(len(queue)):
                word = queue.popleft()
                for j in range(len(word)):
                    for nbr in graph[word[:j] + '*' + word[j+1:]]:
                        if nbr == endWord:
                            return cnt + 1
                        if visited[nbr]:
                            continue

                        queue.append(nbr)
                        visited[nbr] = True

        return 0
