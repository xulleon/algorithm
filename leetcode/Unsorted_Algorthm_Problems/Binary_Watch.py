# https://leetcode.com/problems/binary-watch/
class Solution:

    def readBinaryWatch(self, num: int) -> List[str]:
        '''
        Use DFS to group all combinations of two digits. improve performance by dp
        limit total sum 0-> 11 for hour and 0-59 for minutes.
        '''
        from collections import defaultdict
        hours = [1,2,4,8]
        minutes = [1,2,4,8,16,32]
        dph, dpm = defaultdict(list), defaultdict(list)
        dph[0], dpm[0] = ['0'], ['00']
        dph[1], dpm[1] = [str(k) for k in hours], [str(k).zfill(2) for k in minutes]
        res = []
        for nh in range(2, num + 1):
            if nh in dph:
                continue
            self.helper(hours, 0, [], nh, 'hours', dph)

        for nm in range(2, num + 1):
            if nm in dpm:
                continue
            self.helper(minutes, 0, [], nm, 'minutes', dpm)

        for nh in range(num + 1):
            for hour in dph[nh]:
                nm = num - nh
                for minute in dpm[nm]:
                    res.append(hour + ':' + minute)
        return res


    def helper(self, nums, index, subsets, n, dtype, dp):
        if len(subsets) == n:
            val = sum(subsets)
            if dtype == 'minutes':
                if val < 60:
                    dp[n].append(str(val).zfill(2))
            else:
                if val < 12:
                    dp[n].append(str(val))
            return

        for i in range(index, len(nums)):
            subsets.append(int(nums[i]))
            self.helper(nums, i+1, subsets, n, dtype, dp)
            subsets.pop()

