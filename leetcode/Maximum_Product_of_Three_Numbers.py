# https://leetcode.com/problems/maximum-product-of-three-numbers/submissions/
from functools import reduce
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return reduce((lambda x, y: x*y), nums)

        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])
