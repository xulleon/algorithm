# https://leetcode.com/problems/sum-of-all-odd-length-subarrays/
class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        if len(arr) == 0:
            return 0
        total = sum(arr)
        for delta in range(3, len(arr)+1, 2):
            for start in range(len(arr) - delta + 1):
                total += sum(arr[start: start + delta])

        return total
