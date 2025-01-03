# https://leetcode.com/problems/alien-dictionary/
# Runtime: 56 ms, faster than 55.50% of Python3 online submissions for Alien Dictionary.
"""
This problem has nothing different from other BFS one, other
than how to build_graph. after than, get_indegree and bfs are
the same for rest of BFS problems.
Usually build_graph is different from problem to another. However,
the graph is to create a dictionary that describe the dependency
by using
{a: [a1,a2,a3], b: [b1, b2, b3]} stype dictionary
Input: words = ["wrt","wrf","er","ett","rftt"]
Output: "wertf"
"""
# SOLUTION 1
from collections import defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        wordset = set(''.join(words))

        graph = self.build_graph(words, wordset)
        indegree = self.get_indegree(graph, wordset)
        chars = self.bfs(graph, indegree)
        return chars if len(chars) == len(wordset) else ''

    def build_graph(self, words, wordset):
        # this includes ["aba"] case
        graph = {k:set() for k in wordset}
        for i in range(len(words) - 1):
            # compare two adjacent strings to find lexicographical order
            word1 = words[i]
            word2 = words[i + 1]
            # ["abc", "ab"] special case
            if len(word1) > len(word2) and word1.startswith(word2):
                return {}

            ind = 0
            max_len = min(len(word1), len(word2))
            while ind < max_len and word1[ind] == word2[ind]:
                ind += 1
            else:
                # find the different chars and make the relationship of the two chars
                if ind < max_len:
                    graph[word1[ind]].add(word2[ind])

        return graph

    def get_indegree(self, graph, wordset):
        if not graph:
            return {}
        indegree = {k: 0 for k in wordset}

        for vs in graph.values():
            for v in vs:
                indegree[v] += 1
        return indegree

    def bfs(self, graph, indegree):
        if not graph and not indegree:
            return ''

        res = []
        queue = [k for k, v in indegree.items() if v == 0]
        visited = defaultdict(bool)
        for k in queue:
            visited[k] = True

        while queue:
            char = queue.pop(0)
            res.append(char)
            for nbr in graph[char]:
                if visited[nbr]:
                    continue
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)
                    visited[nbr] = True

        return ''.join(res)

# SOLUTION 2
from collections import deque, defaultdict
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        if len(words) == 0:
            return ''
        
        chars_set = set()
        for word in words:
            chars_set.update(word)
            
        graph = self.build_graph(words, chars_set)
        indegree = self.get_indegree(graph, chars_set)
        return self.bfs(graph, indegree, chars_set)
        
    def build_graph(self, words, chars_set):
        # This is very important!!!
        graph = {k: [] for k in chars_set}
        for i in range(len(words) -1):
            word1, word2 = words[i], words[i+1]
            
            if len(word1) > len(word2) and word1.startswith(word2):
                return {}
            
            max_len = min(len(word1), len(word2))  
            for j in range(max_len):
                if word1[j] != word2[j]:
                    graph[word1[j]].append(word2[j])
                    break

        return graph
    
    def get_indegree(self, graph, chars_set):
        # This is very important!!!
        indegree = {k: 0 for k in chars_set}
            
        for vs in graph.values():
            for v in vs:
                indegree[v] += 1

        return indegree
    
    def bfs(self, graph, indegree, chars_set):
        if not graph:
            return ''
        
        starts = [k for k in indegree if indegree[k] == 0]
        queue = deque(starts)
        res = []
        while queue:
            head = queue.popleft()
            res.append(head)
            for nbr in graph[head]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)
                    
        return ''.join(res) if len(res) == len(chars_set) else ''
