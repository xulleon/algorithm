# https://leetcode.com/problems/excel-sheet-column-title/
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        print(columnNumber)
        if columnNumber == 0:
            return ''

        return self.convertToTitle(columnNumber//27 if columnNumber % 26 == 0 else columnNumber // 26) + chr(64 + (26 if columnNumber % 26 == 0 else columnNumber % 26))
