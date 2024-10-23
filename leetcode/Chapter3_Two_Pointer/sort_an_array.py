# https://leetcode.com/problems/sort-an-array/
# Merge Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if nums is None or n == 0:
            return
        tmp = [0] * n
        self.mergesort(nums, 0, n - 1, tmp)
        return nums
    
    def mergesort(self, nums, start, end, tmp):
        if start >= end:
            return
        
        left, right = start, end
        mid = (start + end) // 2
        
        self.mergesort(nums, start, mid, tmp)
        self.mergesort(nums, mid + 1, end, tmp)
        self.merge(nums, start, end, tmp)
        
    def merge(self, nums, start, end, tmp):
        mid = (start + end) // 2
        left_start, tmp_start, right_start = start, start, mid + 1
        while left_start <= mid and right_start <= end:
            if nums[left_start] <= nums[right_start]:
                tmp[tmp_start] = nums[left_start]
                left_start += 1
            else:
                tmp[tmp_start] = nums[right_start]
                right_start += 1
            tmp_start += 1
            
        while left_start <= mid:
            tmp[tmp_start] = nums[left_start]
            left_start += 1
            tmp_start += 1
            
        while right_start <= end:
            tmp[tmp_start] = nums[right_start]
            right_start += 1
            tmp_start += 1

        for i in range(start, end + 1):
            nums[i] = tmp[i]

# Quick Sort
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if nums == None or len(nums) == 0:
            return
        
        self.quicksort(nums, 0, len(nums) - 1)
        return nums
    
    def quicksort(self, nums, start, end):
        
        if start >= end:
            return
        
        left, right = start, end
        pivot = nums[start + (end - start) // 2]
        
        while left <= right:
            while left <= right and nums[left] < pivot:
                left += 1
                
            while left <= right and nums[right] > pivot:
                right -= 1 
                
            if left <= right:
                nums[left], nums[right] =  nums[right], nums[left]
                left += 1
                right -= 1
                
        self.quicksort(nums, start, right)
        self.quicksort(nums, left, end)
