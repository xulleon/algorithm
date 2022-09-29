# https://leetcode.com/problems/find-pivot-index/
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = 0
        leftsum , rightsum = 0, sum(nums[1:])
        while True:
            if leftsum == rightsum:
                return pivot

            pivot += 1
            if pivot > len(nums) - 1:
                break

            leftsum += nums[pivot - 1]
            rightsum -= nums[pivot]

        return -1
