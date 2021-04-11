# https://leetcode.com/problems/minimum-cost-to-connect-sticks/
# Solution One: using heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        return self.helper(sticks, 0)

    def helper(self, sticks, cost):
        if len(sticks) < 2:
            return cost

        cur_cost = heapq.heappop(sticks) + heapq.heappop(sticks)
        cost += cur_cost
        heapq.heappush(sticks, cur_cost)

        return self.helper(sticks, cost)

# Solution Two: using Priority Queue. performance is not as
# good as the first solution. the conversion from sticks to
# pq took too long time
from queue import PriorityQueue
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        pq = PriorityQueue()
        for stick in sticks:
            pq.put(stick)
        return self.helper(pq, 0)

    def helper(self, pq, cost):
        if pq.qsize() < 2:
            return cost

        cur_cost = pq.get() + pq.get()
        pq.put(cur_cost)
        return self.helper(pq, cost + cur_cost)
