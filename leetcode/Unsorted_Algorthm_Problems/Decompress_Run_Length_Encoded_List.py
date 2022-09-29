# https://leetcode.com/problems/decompress-run-length-encoded-list/submissions/
class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        res = []
        while nums:
            freq, val = nums.pop(0), nums.pop(0)
            res.extend([val] * freq)
        return res
