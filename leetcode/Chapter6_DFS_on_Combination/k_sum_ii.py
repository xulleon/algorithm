# https://www.lintcode.com/problem/90/
# 488 ms time cost· 5.06 MB memory cost· Your submission beats 64.40 % Submissions
class Solution:
    """
    @param a: an integer array
    @param k: a postive integer <= length(A)
    @param target: an integer
    @return: A list of lists of integer
             we will sort your return value in output
    """
    def k_sum_i_i(self, a: List[int], k: int, target: int) -> List[List[int]]:
        # write your code here
        if a == [] or k == 0 or k > len(a):
            return 0
        results = []
        self.dfs(a, 0, [], target, k, results)
        return results

    def dfs(self, nums, index, subsets, target, k, results):
        if target == 0 and len(subsets) == k:
            results.append(subsets)

        for i in range(index, len(nums)):
            if len(subsets) + 1 > k:
                return

            num = nums[i]
            if num > target:
                return
                
            subsets.append(num)
            self.dfs(nums, i + 1, subsets[:], target - num, k, results)
            subsets.pop()
