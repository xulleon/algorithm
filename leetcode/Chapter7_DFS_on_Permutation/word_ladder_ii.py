# https://leetcode.com/problems/word-ladder-ii/
# 9 ms Beats 71.97% 18.31 MB Beats 14.14%

from collections import deque, defaultdict
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
        if beginWord not in wordList:
            wordList.append(beginWord)
        outputs = []
        # Find the graph, which shows the connection of each node to other nodes.
        # describe the neighbor relationships
        graph = self.build_graph(wordList)
        # use bfs from beginWord to endWord to find the level relationship to the endWord
        # remember it is to the beginWord. with the word_level, the code can find which group
        # of the nodes have the same distance to the endWord. It is important that the same distance
        # to the beginWord does not mean the same as the distance to the endWord from BFS perspective!!!
        word_level = self.bfs(beginWord, endWord, graph)
        visited = defaultdict(bool)
        visited[endWord] = True
        # from the above comments, we start to search from endWord to beginWord!!!
        # if we start from beginWord, it will cause TIME LIMIT EXCEEDING!!!
        self.dfs(beginWord, endWord, [endWord], visited, word_level, graph, outputs)
        return outputs

    def build_graph(self, wordList):
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                graph[word[:i] + '*' + word[i+1:]].append(word)
        return graph

    def bfs(self, beginWord, endWord, graph):
        queue = deque()
        queue.append(beginWord)
        visited = defaultdict(bool)
        visited[beginWord] = True
        level = 0
        word_level = defaultdict(int)
        while queue:
            size = len(queue)
            level += 1
            for i in range(size):
                word = queue.popleft()
                word_level[word] = level
                for j in range(len(word)):
                    for nbr in graph[word[:j] + '*' + word[j+1:]]:
                        if visited[nbr]:
                            continue

                        queue.append(nbr)
                        visited[nbr] = True

        return word_level

    def dfs(self, beginWord, endWord, subsets, visited, word_level, graph, outputs):
        if beginWord == endWord:
            outputs.append(subsets[::-1])
            return

        for i in range(len(endWord)):
            new_word = endWord[:i] + '*' + endWord[i+1:]
            for nbr in graph[new_word]:
                if visited[nbr]:
                    continue

                # bfs from beginWord to endWord, dfs is the oppsite direction. Therefore
                # in some cases, the nbrs from endWord to beginWord may not exists in the 
                # word_level
                if nbr in word_level and word_level[endWord] == word_level[nbr] + 1:
                    # only do one leve forward
                    subsets.append(nbr)
                    visited[nbr] = True
                    # subsets need to be a copy, but visited does not as it records the correct 
                    # information 
                    self.dfs(beginWord, nbr, subsets[:], visited, word_level, graph, outputs)
                    subsets.pop()
                    visited[nbr] = False
