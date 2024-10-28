# https://leetcode.com/problems/binary-search/
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Binary Search.
# Memory Usage: 17.7 MB, less than 92.42% of Python3 online submissions for Binary Search.
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 0:
            return -1
        
        return self.binary_search(nums, 0, n - 1, target)
    
    def binary_search(self, nums, start, end, target):
        # step 1: it is start + 1 < end, not start < end
        while start + 1 < end:
            # step 2: mid is calculated inside the while 
            # loop not like bfs before the while loop
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid
                
        # step 3: check both start and end
        if nums[start] == target:
            return start
        
        if nums[end] == target:
            return end
        
        # Step 4: don't forget to return -1 if nothing is found.
        return -1
