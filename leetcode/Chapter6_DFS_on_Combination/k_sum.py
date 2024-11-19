# https://www.lintcode.com/problem/89/description
# 
class Solution:
    """
    @param a: An integer array
    @param k: A positive integer (k <= length(A))
    @param target: An integer
    @return: An integer
    """
    def k_sum(self, a: List[int], k: int, target: int) -> int:
        # write your code here
        if a == [] or k == 0 or target == 0:
            return 0


        results = []
        self.dfs(a, 0, [], k, target, results)
        return len(results)

    def dfs(self, nums, index, subsets, k, target, results):
        if target == 0 and len(subsets) == k:
            results.append(subsets)

        for i in range(index, len(nums)):
            num = nums[i]
            if num > target or len(subsets) + 1 > k:
                break

            subsets.append(num)
            self.dfs(nums, i + 1, subsets[:], k, target - num, results)
            subsets.pop()
