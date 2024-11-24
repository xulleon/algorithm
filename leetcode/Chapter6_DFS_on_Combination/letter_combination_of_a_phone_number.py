# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Letter Combinations of a Phone Number.
# Memory Usage: 16.7 MB, less than 11.31% of Python3 online submissions for Letter Combinations of a Phone
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone = {
            '0': [],
            '1': [],
            '2': ['a', 'b', 'c'],
            '3': ['d','e','f'],
            '4': ['g','h','i'],
            '5': ['j','k','l'],
            '6': ['m','n','o'],
            '7': ['p','q','r', 's'],
            '8': ['t','u','v'],
            '9': ['w','x','y', 'z']
        }
        if len(digits) == 0:
            return []
        
        outputs = []
        visited = [False] * len(digits)
        self.dfs(digits, 0, [], phone, outputs)
        return outputs
    
    def dfs(self, digits, index, subsets, phone, outputs):
        n = len(digits)
        if n == len(subsets):
            outputs.append(''.join(subsets))
            return
        
        for i in range(index, n):
            chars = phone[digits[i]]
            
            for char in chars:
                subsets.append(char)
                self.dfs(digits, i + 1, subsets[:], phone, outputs)
                subsets.pop()
