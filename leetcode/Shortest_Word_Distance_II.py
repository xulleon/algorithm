# https://leetcode.com/problems/shortest-word-distance-ii/
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.wordsDict = wordsDict
        self.len = len(wordsDict)
        self.dp = {word: [] for word in set(wordsDict)}

    def shortest(self, word1: str, word2: str) -> int:
        if self.dp[word1] == []:
            start = self.wordsDict.index(word1)
            end = self.len - 1 - list(reversed(self.wordsDict)).index(word1)
            self.dp[word1] = [ind for ind in range(start, end + 1) if self.wordsDict[ind] == word1]
        if self.dp[word2] == []:
            start = self.wordsDict.index(word2)
            end = self.len - 1 - list(reversed(self.wordsDict)).index(word2)
            self.dp[word2] = [ind for ind in range(start, end + 1) if self.wordsDict[ind] == word2]
        dis = float('inf')
        for ind1 in self.dp[word1]:
            for ind2 in self.dp[word2]:
                if ind1 == ind2:
                    return 0
                dis = min(dis, abs(ind1 - ind2))

        return dis

