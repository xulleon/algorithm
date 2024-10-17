# Unidirectional BFS (beats 73.87% of submission)

from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord is None or len(wordList) == 0 or endWord not in wordList:
            return 0
        
        if beginWord == endWord:
            return 1
        
        graph = self.build_graph(endWord, wordList)
        return self.bfs(graph, beginWord, endWord)
    
    def build_graph(self, endWord, wordList):
        graph = defaultdict(list)
        
        for word in wordList:
            for i in range(len(word)):
                graph[word[:i] + '*' + word[i+1:]].append(word)
                
        return graph
    
    def bfs(self, graph, beginWord, endWord):
        queue = deque([(beginWord, 1)])
        visited = set()
        visited = defaultdict(bool)
        visited[beginWord] = True
        while queue:
            size = len(queue)
            for _ in range(size):
                word, level = queue.popleft()
                for i in range(len(word)):
                    for nbr in graph[word[: i] + '*' + word[i + 1: ]]:
                        if nbr == endWord:
                            return level + 1
                        if visited[nbr]:
                            continue
                        
                        queue.append((nbr, level + 1))
                        visited[nbr] = True
                        
        return 0



# Bidirectional BFS (Runtime: 101 ms, faster than 97.14% of Python3 online submissions for Word Ladder.)

from collections import deque, defaultdict
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if beginWord is None or len(wordList) == 0 or endWord not in wordList:
            return 0
        
        if beginWord == endWord:
            return 1
        
        graph = self.build_graph(wordList)
        return self.bfs(graph, beginWord, endWord)
    
    def build_graph(self, wordList):
        graph = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                graph[word[:i] + '*' + word[i+1:]].append(word)
                
        return graph
    
    def bfs(self, graph, beginWord, endWord):
        src_queue = deque([beginWord])
        end_queue = deque([endWord])
        src_visited = defaultdict(bool)
        end_visited = defaultdict(bool)
        
        src_visited[beginWord] = True
        end_visited[endWord] = True
        cnt = 1
        while src_queue and end_queue:
            src_size, end_size = len(src_queue), len(end_queue)
            
            cnt += 1
            for i in range(src_size):
                word = src_queue.popleft()
                for j in range(len(word)):
                    for nbr in graph[word[:j] + '*' + word[j+1:]]:
                        if end_visited[nbr]:
                            return cnt
                        
                        if src_visited[nbr]:
                            continue
                            
                        src_queue.append(nbr)
                        src_visited[nbr] = True
                        
            cnt += 1
            for i in range(end_size):
                word = end_queue.popleft()
                for j in range(len(word)):
                    for nbr in graph[word[:j] + '*' + word[j+1:]]:
                        if src_visited[nbr]:
                            return cnt
                        
                        if end_visited[nbr]:
                            continue
                            
                        end_queue.append(nbr)
                        end_visited[nbr] = True
                            
        return 0
