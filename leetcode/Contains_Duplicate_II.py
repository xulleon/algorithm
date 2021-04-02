# https://leetcode.com/problems/contains-duplicate-ii/
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import defaultdict
        numdict = defaultdict(list)
        for ind, v in enumerate(nums):
            numdict[v].append(ind)

        print(numdict)
        diff = 0
        for vs in numdict.values():
            if len(vs) == 1:
                continue
            if self.getdiff(vs, k):
                return True

        return False

    def getdiff(self, indexes, k):
        indexes.sort()
        min_diff = -float('inf')
        for i in range(1, len(indexes)):
            if abs(indexes[i-1] - indexes[i]) <= k:
                return True

        return False
