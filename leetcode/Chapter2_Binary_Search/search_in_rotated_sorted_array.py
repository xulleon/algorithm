# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Search in Rotated Sorted Array.
# Memory Usage: 17.1 MB, less than 12.92% of Python3 online submissions for Search in Rotated Sorted Array.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        if n == 1:
            return 0 if nums[0] == target else -1
        
        if n == 2:
            if nums[0] != target and nums[1] != target:
                return -1
            else:
                return 0 if nums[0] == target else 1
            
        start, end = 0, n - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if target >= nums[0]:
                # The target is at left part
                if nums[mid] >= target:
                    # mid is at right of target
                    end = mid
                else:
                    if nums[mid] >= nums[0]:
                        # mid is at left part but lower than target
                        start = mid
                    else:
                        # mid is at right part
                        end = mid
            else:
                # Target at the right part
                if nums[mid] >= nums[0]:
                    # mid is at left side, therefore, move start to mid
                    start = mid
                else: #if nums[mid] <= nums[n - 1]:
                    if nums[mid] <= target:
                        # mid is at the right side and below target
                        start = mid
                    else:
                        # mid is at the right side and above target
                        end = mid
                
        if nums[start] == target:
            return start
        
        if nums[end] == target:
            return end
        
        return -1
