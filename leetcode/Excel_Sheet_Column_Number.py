# https://leetcode.com/problems/excel-sheet-column-number/
class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        columnTitle = list(columnTitle)
        mul, count, base = 0, 0, ord('A')
        while columnTitle:
            char = columnTitle.pop()
            count += (ord(char) - base + 1) * (26**mul)
            mul += 1
        return count
