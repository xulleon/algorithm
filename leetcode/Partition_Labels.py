#  solution one: low performance, Runtime: 140 ms, faster than 5.13%
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res = []
        self.helper(S, res)
        return res

    def helper(self, S, res):
        if len(S) == 0:
            return
        if len(S) == 1:
            res.append(1)
            return

        for i in range(1, len(S) + 1):
            if set(S[:i]).intersection(set(S[i:])):
                continue
            else:
                res.append(len(S[:i]))
                self.helper(S[i:], res)
                break

# Solution two: very good technique to find a char last occurance index
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        res = []
        # Find the max ind of a char in a string. need to remember it
        dp = {char: ind for ind, char in enumerate(S)}
        p0 = p1 = 0
        for i in range(len(S)):
            p1 = max(p1, dp[S[i]])
            if i == p1:
                # Foudn a group
                res.append(p1 - p0 + 1)
                p0 = i + 1

        return res
