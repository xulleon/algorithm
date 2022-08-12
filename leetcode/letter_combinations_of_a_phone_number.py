# https://leetcode.com/problems/letter-combinations-of-a-phone-number/submissions/

phones = {
    '0': [],
    '1': [],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g','h','i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
}


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        results = []
        if digits == '':
            return results

        visited = [False] * len(digits)
        self.dfs(digits, phones, 0, [], results, visited)
        return [''.join(k) for k in results]

    def dfs(self, digits, phones, index, subsets, results, visited):

        if len(digits) == len(subsets):
            results.append(subsets)
            return

        for i in range(index, len(digits)):
            if visited[i]:
                continue
            for char in phones[digits[i]]:
                subsets.append(char)
                visited[i] = True
                self.dfs(digits, phones, i+1, subsets[:], results, visited)
                subsets.pop()
                visited[i] = False
