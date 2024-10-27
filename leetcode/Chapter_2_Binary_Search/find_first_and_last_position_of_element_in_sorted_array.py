# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
# Memory Usage: 18.1 MB, less than 14.28% of Python3 online submissions for Find First and Last Position of Element in Sorted Array.
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return [-1, -1]
        
        first = self.binary_search(nums, 0, n - 1, target)
        
        if first == -1:
            return [-1, -1]
        
        last = first
        while last < n and nums[last] == target:
            last += 1
            
        last -= 1
        return [first, last]
        
    def binary_search(self, nums, start, end, target):
        # step 1: ensure the condition is start + 1 < end!!!
        while start + 1 < end:
            # different from bfs, binary search mid is inside the while loop
            mid = (start + end) // 2
            if nums[mid] >= target:
                end = mid
            else:
                start = mid
        
        if nums[start] == target:
            return start
            
        if nums[end] == target:
            return end
        
        return -1
