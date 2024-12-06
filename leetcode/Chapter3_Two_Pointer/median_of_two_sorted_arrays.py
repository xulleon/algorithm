# https://leetcode.com/problems/median-of-two-sorted-arrays/
# Solution 1 - heapq
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

# Solution 2 - mergesort
# Runtime: 3 ms, faster than 53.22% of Python3 online submissions for Median of Two Sorted Arrays.
# Memory Usage: 17.5 MB, less than 13.27% of Python3 online submissions for Median of Two Sorted Arrays.
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        First use partial merge sort to merge to lists together
        second, get the median
        '''
        n, m = len(nums1), len(nums2)
        tmp = [0] * (m + n)
        left_start, tmp_start, right_start = 0, 0, 0
        while left_start < n and right_start < m:
            if nums1[left_start] <= nums2[right_start]:
                tmp[tmp_start] = nums1[left_start]
                left_start += 1
            else:
                tmp[tmp_start] = nums2[right_start]
                right_start += 1
            tmp_start += 1
            
        while left_start < n:
            tmp[tmp_start] = nums1[left_start]
            left_start += 1
            tmp_start += 1
        
        while right_start < m:
            tmp[tmp_start] = nums2[right_start]
            right_start += 1
            tmp_start += 1
        
        half = (m + n) // 2
        if (m + n) %2 == 0:
            return (tmp[half - 1] + tmp[half]) / 2
        else:
            return tmp[half]
