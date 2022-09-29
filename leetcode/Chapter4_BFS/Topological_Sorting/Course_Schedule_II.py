from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if not prerequisites:
            return [k for k in range(numCourses)]

        course_set = set([k for k in range(numCourses)])
        # for prereq in prerequisites:
        #     course_set.update(prereq)

        graph = self.build_graph(prerequisites)
        indegree = self.get_indegree(graph, course_set)
        courses = self.bfs(graph, indegree)
        return courses if len(courses) == numCourses else []

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
        res = []
        visited = defaultdict(bool)
        for k in queue:
            visited[k] = True

        while queue:
            course = queue.pop(0)
            res.append(course)
            for nbr in graph[course]:
                if visited[nbr]:
                    continue

                indegree[nbr] -= 1
                if indegree[nbr] == 0:
                    queue.append(nbr)
                    visited[nbr] = True

        return res
