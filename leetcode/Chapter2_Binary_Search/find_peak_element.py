# https://leetcode.com/problems/find-peak-element/
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Find Peak Element.
# Memory Usage: 16.8 MB, less than 35.87% of Python3 online submissions for Find Peak Element.
class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0:
            return None
        
        if n == 1:
            return 0
        
        if n == 2:
            return 0 if nums[0] >= nums[1] else 1

        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] <=  nums[mid + 1]:
                start = mid
            elif nums[mid] > nums[mid + 1]:
                end = mid
                
        return start if nums[start] >= nums[end] else end
