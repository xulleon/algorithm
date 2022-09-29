# https://leetcode.com/problems/course-schedule/
# Runtime: 118 ms, faster than 82.38% of Python3 online submissions for Course Schedule.
'''
Topological Sorting includes
1) build graph
2) get indegree
3) bfs
 3.1) add indegree 0 items into a queue
 3.2) while loop the queue
 3.3) popleft the item from the queue
 3.4) for loop the nbrs of the item (from graph built at step 1)
 3.5) check if this nbr has been visited
 3.6) decrease the nbr's indegree
 3.7) if the nbr's indegree is zero, append the nbr into the queue
'''
from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True

        course_set = set()
        for req in prerequisites:
            course_set.update(req)

        graph = self.build_graph(prerequisites)
        indegree = self.get_indegree(graph, course_set)
        courses = self.bfs(graph, indegree)
        return True if len(courses) == len(course_set) else False

    def build_graph(self, prerequisites):
        graph = defaultdict(list)

        for prereq in prerequisites:
            graph[prereq[1]].append(prereq[0])

        return graph

    def get_indegree(self, graph, course_set):
        indegree = {k: 0 for k in course_set}
        for vs in graph.values():
            for v in vs:
                indegree[v] += 1
        return indegree

    def bfs(self, graph, indegree):

        queue = [k for k, v in indegree.items() if v == 0]
        visited = defaultdict(bool)
        for k in queue:
            visited[k] = True
        res = []
        while queue:
            head = queue.pop(0)
            res.append(head)
            for nbr in graph[head]:
                indegree[nbr] -= 1
                if visited[nbr]:
                    continue
                if indegree[nbr] == 0:
                    queue.append(nbr)
                    visited[nbr] = True

        return res
