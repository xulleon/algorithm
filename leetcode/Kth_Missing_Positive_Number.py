# https://leetcode.com/problems/kth-missing-positive-number/
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        n = arr[-1] + k + 1
        return [k for k in range(1, n) if k not in arr][k-1]
