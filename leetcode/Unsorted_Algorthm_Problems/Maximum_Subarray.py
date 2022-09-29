# https://leetcode.com/problems/maximum-subarray/
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = cur_sum = nums[0]
        for num in nums[1:]:
            # if cur_sum less than current value, then forget
            # the previous elements as it only reduce the total sum
            # [-2, 1, -2, 5, 8]. when point to index 1 values,
            # the cur_val is -1 but current value is 1, then we
            # can forget the first element "-2". The same when
            # point to the idex 3 (value 5), the cur_sum is -2,
            # the current value is 5, then we can forget elements
            # from index 0 to 2. instead use 5, therefore, the
            # latest cur_sum is 5, max_sum is also 5. with next
            # element 8, then the max sum will be 13.
            cur_sum = max(cur_sum + num, num)
            max_sum = max(max_sum, cur_sum)
        return max_sum
