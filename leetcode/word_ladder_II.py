# https://leetcode.com/problems/word-ladder-ii/submissions/
from pprint import pprint
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return []

        ladder = []
        if beginWord not in wordList:
            # THIS IS VERY IMPORTANT!!!
            wordList.append(beginWord)
        indegree = self.build_graph(wordList)
        distance = self.bfs(beginWord, indegree)
        self.dfs(ladder, [endWord], endWord, beginWord, indegree, distance)

        return ladder

    def dfs(self, ladder, subsets, end, start, indegree, distance):
        if end == start:
            # This is an exit condition
            ladder.append(subsets[::-1])
            return

        for i in range(len(end)):
            # it is important to track from end to start
            new_end = end[:i] + '*' + end[i+1:]
            for word in indegree[new_end]:
                if word in subsets:
                    # ensure that nbr is never used.
                    continue
                # this condition ensure that the path is going to the direction
                # to the endWord, not going back or stay in the same level!!!!!
                # this is another reasaon why we need bfs to create the distance dict
                if distance[word] + 1 == distance[end]:
                    subsets.append(word)
                    self.dfs(ladder, subsets[:], word, start, indegree, distance)
                    subsets.pop()

    # different from word ladder. this problem requires to list possible pathes
    # bfs is needed to create the instance dictionary. This dict will record
    # the cost of each node from beginWord to endWord
    def bfs(self, beginWord, indegree):
        from collections import deque
        queue = deque([(beginWord, 1)])
        instance = {beginWord: 1}
        visited = {beginWord: True}
        while queue:
            size = len(queue)
            for _ in range(size):
                word, level = queue.popleft()
                for i in range(len(word)):
                    new_word = word[:i] + '*' + word[i+1:]
                    for nbr in indegree[new_word]:
                        if nbr not in instance:
                            # append a tuple (nbr, level+1) on queue!!!!!
                            queue.append((nbr, level + 1))
                            instance[nbr] = level + 1
        return instance


    # Template to build a tree with strings
    # Need to memorize it.
    def build_graph(self, wordList):
        from collections import defaultdict
        indegree = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                new_word = word[:i] + '*' + word[i+1:]
                indegree[new_word].append(word)
        return indegree


