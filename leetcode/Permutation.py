# https://leetcode.com/problems/permutations/
# Runtime: 40 ms, faster than 95.32% of Python3 online submissions for Permutations.
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        results = []
        visited = [False] * len(nums)
        self.dfs(nums, 0, [], results, visited)
        return results

    def dfs(self, nums, index, subsets, results, visited):
        if len(nums) == len(subsets):
            results.append(subsets)

        for i in range(len(nums)):
            # permutation is directional connection. Therefore, [1,2] and [2,1] are different.
            # i always starts from 0. Combination is different, it will start from index to len(nums) - 1
            if visited[i]:
                # visited is used to prevent a number being used multiple times.
                continue

            subsets.append(nums[i])
            visited[i] = True
            self.dfs(nums, i + 1, subsets[:], results, visited)
            subsets.pop()
            visited[i] = False
