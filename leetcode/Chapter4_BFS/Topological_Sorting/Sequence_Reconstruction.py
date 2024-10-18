# https://leetcode.com/problems/sequence-reconstruction/
# Runtime: 1288 ms, faster than 5.01% of Python3 online submissions for Sequence Reconstruction.
'''
If convert the sequences to a graph, it means that at any time, the indegree must be 1, any indegree > 1 will be false.
Therefore, it is a typical BFS on Graph problem. the solution is to
- build a graph
- get indegree
- bfs to solve it.
'''
class Solution:
    def sequenceReconstruction(self, nums: List[int], sequences: List[List[int]]) -> bool:
        num_set = set()
        for seq in sequences:
            num_set.update(seq)
        graph = self.build_graph(sequences, num_set)
        indegree = self.get_indegree(graph, sequences, num_set)
        return self.bfs(indegree, graph, nums)

    def build_graph(self, sequences, num_set):
        graph = {k: set() for k in num_set}

        for seq in sequences:
            for i in range(len(seq) - 1):
                graph[seq[i]].add(seq[i + 1])
        return graph

    def get_indegree(self, graph, sequences, num_set):
        indegree = {k: 0 for k in num_set}
        for vs in graph.values():
            for v in vs:
                indegree[v] += 1

        return indegree

    def bfs(self, indegree, graph, nums):
        queue = [k for k, v in indegree.items() if v == 0]
        res = []
        while queue:
            if len(queue) > 1:
                return []

            head = queue.pop(0)
            res.append(head)
            for nbr in graph[head]:
                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)

        return res == nums

