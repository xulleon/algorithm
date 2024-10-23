# https://leetcode.com/problems/top-k-frequent-elements/
# Runtime: 7 ms, faster than 97.06% of Python3 online submissions for Top K Frequent Elements.
# Memory Usage: 20 MB, less than 98.94% of Python3 online submissions for Top K Frequent Elements.
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        
        res = defaultdict(int)
        for i in nums:
            res[i] += 1
            
        res = sorted(res, key = res.get, reverse = True)
        return res[:k]
