# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# SOLUTION 1 (Use extra space of visited
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

# SOLUTION 2 - No extra space is used. purely use the existing array
#Runtime: 3 ms, faster than 94.55% of Python3 online submissions for Remove Duplicates from Sorted Array.
# Memory Usage: 17.9 MB, less than 83.04% of Python3 online submissions for Remove Duplicates from Sorted Array.
from collections import defaultdict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return n
        
        # visited = defaultdict(bool)
        found_dup = False
        pl, pr, ptr = 0, n - 1, 0
        while ptr < n:
            # look for the  next new number index
            # if no dup exists, then ptr will go to the end of the array
            if not found_dup and nums[ptr] != nums[ptr + 1]:
                ptr += 1
  
            while ptr < n - 1 and nums[ptr] == nums[ptr + 1]:
                # at least one dup is found
                found_dup = True
                nums[ptr] = '_'
                ptr += 1

            if found_dup:
                while pl < n and nums[pl] != '_':
                    # once a dup is found, then there is at least one '_'
                    # find the first '_' index
                    pl += 1

                if pl < n - 1 and pl < ptr:
                    nums[pl], nums[ptr] = nums[ptr], nums[pl]
                    pl += 1
                    ptr += 1
                
            if not found_dup and ptr == n - 1:
                # No dup found in the array
                return n

        return pl
