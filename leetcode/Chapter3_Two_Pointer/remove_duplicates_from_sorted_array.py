# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 17.9 MB, less than 82.93% of Python3 online submissions for Remove Duplicates from Sorted Array.
from collections import defaultdict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return [] if n == 0 else 1
        
        visited = defaultdict(bool)
        # pl to point the first '_' while ptr looking for the next non '_' value
        pl, ptr, k = 0, 0, 0

        # make all duplicated value as '_', using visited
        for i in range(n):
            if visited[nums[i]]:
                nums[i] = '_'
            else:
                visited[nums[i]] = True
                
        while ptr < n:
            # Find the next '_' index
            while pl < n and nums[pl] != '_':
                pl += 1

            # if ptr <= pl, skip and jump to the index next to pl
            if ptr <= pl:
                ptr = pl + 1

            # find next non '_' value
            while ptr < n and nums[ptr] == '_':
                ptr += 1
                
            if ptr < n:
                # swap a non '_' value with a '_'
                nums[ptr], nums[pl] = nums[pl], nums[ptr]
                
        return len(visited.keys())
