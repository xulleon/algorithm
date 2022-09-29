#  https://leetcode.com/problems/permutations-ii/submissions/
# Runtime: 89 ms, faster than 65.99% of Python3 online submissions for Permutations II.
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        results = []
        nums.sort()
        visited = [False] * len(nums)
        self.dfs(nums, [], results, visited)
        return results

    def dfs(self, nums, subsets, results, visited):
        if len(subsets) == len(nums):
            results.append(subsets)
            return

        for i in range(len(nums)):
            # the permutation is different than combination is that the range always starts from 0
            # use visited list to track which value has already been used
            if visited[i]:
                continue

            # if there are duplicated values, ensure that it always starts from the lower index
            # i.e. [1,1,2]. It will never start with the second 1 before first 1. This is what the
            # condition below is.
            if i > 0 and nums[i-1] == nums[i] and not visited[i-1]:
                continue

            subsets.append(nums[i])
            visited[i] = True
            self.dfs(nums, subsets[:], results, visited)
            subsets.pop()
            visited[i] = False
