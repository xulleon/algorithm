# https://leetcode.com/problems/longest-harmonious-subsequence/
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        '''
        Thd idea is to first get result of Counter.
        then from hight to lowe, if the ajacent two
        numbers have 1 differencem then add the occurance
        numbers of both. with one single loop to get a result. O(n)
        :param nums:
        :return:
        '''
        from collections import Counter
        numdict = Counter(nums)
        keys = sorted(numdict)
        maxcount = 0
        for i in range(len(keys)-1, 0, -1):
            if keys[i] - keys[i-1] == 1:
                maxcount = max(maxcount, numdict[keys[i]] + numdict[keys[i-1]])
        return maxcount
