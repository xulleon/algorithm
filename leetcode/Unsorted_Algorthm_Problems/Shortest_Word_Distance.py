# https://leetcode.com/problems/shortest-word-distance/
# Solution One: Better performance. took 56 ms
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        if len(wordsDict) == 0:
            return 0

        from collections import defaultdict
        dp = defaultdict(set)
        for index, word in enumerate(wordsDict):
            if word in [word1, word2]:
                dp[word].add(index)

        if not dp[word1] or not dp[word2]:
            return -1

        diff = float('inf')
        for i in dp[word1]:
            for j in dp[word2]:
                diff = min(diff, abs(i - j))

        return diff

# Solution Two: took 68 ms
class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        diff = float('inf')
        index1, index2 = -1, -1

        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                index1 = i
            if wordsDict[i] == word2:
                index2 = i
            if index1 != -1 and index2 != -1:
                diff = min(diff, abs(index1 - index2))
        return diff
