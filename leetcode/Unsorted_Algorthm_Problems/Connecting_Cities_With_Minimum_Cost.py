# https://leetcode.com/problems/connecting-cities-with-minimum-cost/
class Solution:
    '''
    Kruskals algorithm for MST - Minimum Spanning Tree
    '''
    def minimumCost(self, N: int, connections: List[List[int]]) -> int:
        connections.sort(key=lambda grp: (grp[2], grp[0], grp[1]))
        self.count, self.cost, self.father, res = 0, 0, {}, []
        self.father = {i:i for i in range(1, N + 1)}
        #self.initialize(connections)
        for conn in connections:
            if self.union(conn):
                self.cost += conn[2]
        if self.count == N - 1:
            return self.cost

        return -1

    def initialize(self, connections):
        for connection in connections:
            city1, city2, cost = connection
            if city1 not in self.father:
                self.father[city1] = city1

            if city2 not in self.father:
                self.father[city2] = city2


    def union(self, conn):
        city1, city2 = conn[0], conn[1]
        root1 = self.find(city1)
        root2 = self.find(city2)
        if root1 != root2:
            # here use root1/root2 instead of city1/city2
            # this is the way as how to know if a vertex
            # has been processed or not.
            self.father[root1] = root2
            self.count += 1
            return True
        # means that both cities has a common father
        # means they already connected. a loop will be
        # created if both cities are connect3ed.
        return False

    def find(self, city):
        path = []
        while self.father[city] != city:
            path.append(city)
            city = self.father[city]

        for p in path:
            self.father[p] = city
        return city

