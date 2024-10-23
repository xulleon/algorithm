# https://leetcode.com/problems/sort-colors/
# The trick is when swap 2, it may be 0 or 1, therefore, the pointer should be not incremented.
#              when swap 1, pl should not be increased!!!
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if nums is None or len(nums) == 0:
            return []
        
        ptr, pl, pr = 0, 0, n - 1
        while ptr <= pr:
            if nums[ptr] == 0:
                nums[ptr], nums[pl] = nums[pl], nums[ptr]
                ptr += 1
                pl += 1
            elif nums[ptr] == 2:
                # ptr should be not be increased!!! 
                nums[ptr], nums[pr] = nums[pr], nums[ptr]
                pr -= 1
            else:
                ptr += 1
                
        return nums
    
