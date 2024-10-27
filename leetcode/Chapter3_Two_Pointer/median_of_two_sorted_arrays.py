# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Runtime: 4 ms, faster than 35.52% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 16.9 MB, less than 29.62% of Python3 online submissions for Median of Two Sorted Arrays.
from heapq import heappush, heappop, heapify
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        if n == 0 and m == 0:
            return 0
        # left is max heap and right is min heap
        left, right = [], nums1 + nums2
        
        half = (n + m ) // 2
        even = (m + n) % 2 == 0
        
        heapify(right)
        
        for i in range(half):
            heappush(left, -heappop(right))
            
        if even:
            return (-left[0] + right[0]) / 2
        
        return right[0]
