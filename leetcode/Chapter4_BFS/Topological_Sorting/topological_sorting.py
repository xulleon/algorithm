# https://www.lintcode.com/problem/127/description
# This is a typical non-level BFS algorithm
"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""
from collections import deque, defaultdict
class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """
    def topSort(self, graph):
        # write your code here
        if graph is None or len(graph) == 0:
            return []
        
        mygraph = self.build_graph(graph)

        indegree = self.build_indegree(mygraph)
        return self.bfs(mygraph, indegree)

    def build_graph(self, nodes):
        nodes_dict = defaultdict(list)
        for node in nodes:
            if not node:
                continue

            for nbr in node.neighbors:
                if not nbr:
                    continue
                nodes_dict[node].append(nbr)

        return nodes_dict
