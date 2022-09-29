# https://leetcode.com/problems/clone-graph/
# Runtime: 84 ms, faster than 12.22% of Python3 online submissions for Clone Graph.
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import defaultdict
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if node is None:
            return None

        queue = [node]
        visited = {}
        while queue:
            root = queue.pop(0)
            if root not in visited:
                visited[root] = Node(root.val, [])

            for nbr in root.neighbors:
                if nbr not in visited:
                    visited[nbr] = Node(nbr.val, [])
                    queue.append(nbr)
                visited[root].neighbors.append(visited[nbr])

        return visited[node]
