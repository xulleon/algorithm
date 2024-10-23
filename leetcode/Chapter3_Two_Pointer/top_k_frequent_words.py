# https://leetcode.com/problems/top-k-frequent-words/
# Runtime: 5 ms, faster than 94.75% of Python3 online submissions for Top K Frequent Words.
# Memory Usage: 16.6 MB, less than 93.56% of Python3 online submissions for Top K Frequent Words.
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import defaultdict
        dp = defaultdict(int)
        for word in words:
            dp[word] += 1
            
        res = sorted(dp.items(), key = lambda grp: (-grp[1], grp[0]))
        return [res[i][0] for i in range(k)]
