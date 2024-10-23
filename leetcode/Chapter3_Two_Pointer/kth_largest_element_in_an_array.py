# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Runtime: 46 ms, faster than 99.19% of Python3 online submissions for Kth Largest Element in an Array.
# Memory Usage: 27.8 MB, less than 96.97% of Python3 online submissions for Kth Largest Element in an Array.
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if nums is None or len(nums) == 0:
            return None
        
        return self.quick_select(nums, 0, len(nums) - 1, k)
    
    def quick_select(self, nums, start, end, k):
        if start == end:
            return nums[start]
        
        left, right = start, end
        pivot = nums[(start + end) // 2]
        while left <= right:
            
            while left <= right and nums[left] > pivot:
                left += 1
                
            while left <= right and nums[right] < pivot:
                right -= 1
                
            if left <= right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1
                
        if start + k - 1 <= right:
            return self.quick_select(nums, start, right, k)
            
        if start + k - 1 >= left:
            return self.quick_select(nums, left, end, k - (left - start))
        
        return nums[right + 1]
