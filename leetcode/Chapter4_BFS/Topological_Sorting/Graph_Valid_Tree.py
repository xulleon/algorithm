# https://leetcode.com/problems/graph-valid-tree
# Runtime: 102 ms, faster than 89.87% of Python3 online submissions for Graph Valid Tree
'''
In order to resolve this problem,
1) knowledge: if it is a tree, num_nodes - 1 == num_eddges.
2) for this specific problem, the first point is 0, since the problem was given with a list of subsequences, we need to
 - first build a graph
 - traverse the graph to get a list of nodes, ensure the num_nodes found is equal to n.
   - by traverse the graph, it also tells if the graph contains more than one sub-graphs. as there is no way to traverse to the other sub-graphs
'''
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # First check the relationship of nodes and edges
        if n -1 != len(edges):
            return False

        # if the above condition is met, then traverse the graph to see
        # if the number of nodes found is equal to n. It is a basic BFS
        graph = self.build_graph(edges)
        nodes = self.bfs(n, graph)
        return True if n == len(nodes) else False


    def build_graph(self, edges):
        from collections import defaultdict
        graph = defaultdict(list)
        for edge in edges:
            # This is very important to do it bi-directional
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        return graph

    # This is a basic BFS
    def bfs(self, n, graph):
        # Always start from 0. If it is a two graphs, then the second graph
        # will not be able to reach
        queue = [0]
        nodes = []
        visited = {k: False for k in range(n)}
        visited[0] = True
        while queue:
            head = queue.pop(0)
            nodes.append(head)
            for nbr in graph[head]:
                if visited[nbr]:
                    continue

                queue.append(nbr)
                # do not forget update visited, othereise, it will loop itself.
                visited[nbr] = True

        return nodes

