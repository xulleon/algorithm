# https://leetcode.com/problems/verifying-an-alien-dictionary/
class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dp = {k: ind for ind, k in enumerate(order)}
        for i in range(1, len(words)):
            if words[i-1] != words[i] and words[i] in words[i-1]:
                # check if ['apple', 'app']
                return False

            for j in range(min(len(words[i-1]), len(words[i]))):
                if dp[words[i-1][j]] > dp[words[i][j]]:
                    return False

                if dp[words[i-1][j]] < dp[words[i][j]]:
                    # if char follows the order, move to next pair of words
                    break

        return True
