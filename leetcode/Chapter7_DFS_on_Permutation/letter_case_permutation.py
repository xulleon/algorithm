# https://leetcode.com/problems/letter-case-permutation/
# https://www.youtube.com/watch?v=_Ipng-tBpSw
# This is not dfs permutation algorithm!!!
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Letter Case Permutation.
# Memory Usage: 17.2 MB, less than 97.88% of Python3 online submissions for Letter Case Permutation.
class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = ['']
        for char in s:
            char = char.lower()
            tmp = []
            for op in output:
                tmp.append(op + char)
                if char.isalpha():
                    tmp.append(op + char.upper())
            output = tmp
                
        return output
