# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/submissions/
# Runtime: 3 ms, faster than 100.00% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
# Memory Usage: 17 MB, less than 20.11% of Python3 online submissions for Find Minimum in Rotated Sorted Array.
class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return nums[0]
        
        if nums[n -1 ] > nums[0]:
            return nums[0]
        
        start, end = 1, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] > nums[0]:
                start = mid
            elif nums[mid] < nums[n-1]:
                end = mid
            
        return min(nums[start], nums[end])
