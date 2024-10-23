# https://leetcode.com/problems/two-sum/
# Solution 1
# Runtime: 926 ms, faster than 33.83% of Python3 online submissions for Two Sum.
# Memory Usage: 17.3 MB, less than 79.55% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        
        for p1 in range(n - 1):
            residue = target - nums[p1]
            for p2 in range(p1 + 1, n):
                if nums[p2] == residue:
                    return [p1, p2]
                
        return []

# Solution 2
# Runtime: 3 ms, faster than 97.07% of Python3 online submissions for Two Sum.
# Memory Usage: 17.8 MB, less than 15.14% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        
        nums_dict = {num: index for index, num in enumerate(nums)}
        
        for i in range(n):
            comp = target - nums[i]
            try:
                j = nums_dict[comp]
                if i == j:
                    continue

                return [i, j]
            except:
                continue
                
        return []
