# https://leetcode.com/problems/find-median-from-data-stream/
# https://www.youtube.com/watch?v=itmhHWaHupI
import heapq
class MedianFinder:
    slow_ptr = 0
    fast_ptr = 0
    def __init__(self):
        self.low = []
        self.high = []

    def addNum(self, num: int) -> None:
        # always push to the low first
        heapq.heappush(self.low, -num)
        
         # check if the highest value in self.low is greater than the lowest value in self.high
        if (self.low and self.high) and -1 * self.low[0] > self.high[0]:
            val = heapq.heappop(self.low)
            heapq.heappush(self.high, -val)
            
        # check if low and high are balanced
        if len(self.low) > len(self.high) + 1:
            val = -heapq.heappop(self.low)
            heapq.heappush(self.high, val)
            
        if len(self.high) > len(self.low) + 1:
            val = heapq.heappop(self.high)
            heapq.heappush(self.low, -val)
            
    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        if len(self.low) < len(self.high):
            return self.high[0]
                
        return (-self.low[0] + self.high[0]) / 2
