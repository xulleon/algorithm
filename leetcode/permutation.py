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
            if visited[i]:
                continue

            subsets.append(nums[i])
            visited[i] = True
            self.dfs(nums, i + 1, subsets[:], results, visited)
            subsets.pop()
            visited[i] = False
