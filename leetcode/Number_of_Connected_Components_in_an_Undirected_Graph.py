# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
from queue import Queue
from collections import defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = {node: False for node in range(n)}
        graph = self.build_graph(edges)
        count = 0
        for node in range(n):
            if not visited[node]:
                count += 1
                visited[node] = True
                self.bfs(node, graph, visited)

        return count

    def build_graph(self, edges):
        graph = defaultdict(set)
        for pair in edges:
            graph[pair[0]].add(pair[1])
            graph[pair[1]].add(pair[0])
        return graph

    def bfs(self, node, graph, visited):
        q = Queue()
        q.put(node)
        while not q.empty():
            head = q.get()
            for nbr in graph[head]:
                if visited[nbr]:
                    continue
                q.put(nbr)
                visited[nbr] = True

