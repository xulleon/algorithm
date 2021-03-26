# https://leetcode.com/problems/missing-number/
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        '''
        If the nums aligns properly, it should be the
        same as the index value. The exception is for the last number missing
        :param nums:
        :return:
        '''
        nums.sort()
        for i in range(len(nums) + 1):
            try:
                if i != nums[i]:
                    return i
            except:
                return i
