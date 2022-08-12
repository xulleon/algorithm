# https://leetcode.com/problems/word-pattern-ii/submissions/
"""
The idea of the solution is to try the pattern with difference combination
until the pattern characters match one combination which can resolve the matching issue.
Since the answer is a boolean,
"""
class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        result_dict = {}
        result_set = set()
        return self.dfs(pattern, s, result_dict, result_set)

    def dfs(self, pattern, s, result_dict, result_set):
        if len(pattern) == 0:
            return len(s) == 0

        char = pattern[0]
        # if matching exists, then replace the pattern to see if all pattern are matched.
        if char in result_dict:
            if not s.startswith(result_dict.get(char)):
                # this ensures that nonsences will not go any further
                return False
            # this will shorten the s and enventually go to an empty string.
            return self.dfs(pattern[1:], s[len(result_dict.get(char)):], result_dict, result_set)

        # This part is typical DFS
        for i in range(len(s)):
            word = s[:i + 1]
            if word in result_set:
                # since each phrase is a value of the key in result_dict.
                # This ensures that no further DFS is done on the phrase.
                continue
            # This ensure that all the combinations that are potentually an answer can be created.
            result_dict[char] = word
            result_set.add(word)
            if self.dfs(pattern[1:], s[i+1:], result_dict, result_set):
                # This return ensure that once a solution is caught, this DFS is concluded.
                # otherwise, continue looking
                return True
            del result_dict[char]
            result_set.remove(word)
