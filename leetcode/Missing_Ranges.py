# https://leetcode.com/problems/missing-ranges/
class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:
        def assemblyStr(start, end):
            if start == end:
                return str(start)
            else:
                return str(start) + '->' + str(end)

        if len(nums) == 0:
            return [assemblyStr(lower, upper)]

        res = []
        start = end = lower
        for num in nums:
            if start > upper:
                return res

            if start == num:
                start += 1
                continue
            end = num - 1
            res.append(assemblyStr(start, end))
            start = num + 1

        if start > upper:
            return res

        res.append(assemblyStr(start, upper))
        return res

