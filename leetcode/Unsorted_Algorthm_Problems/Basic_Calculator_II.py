# https://leetcode.com/problems/basic-calculator-ii/
class Solution:
    def calculate(self, s: str) -> int:
        if len(s) == 0:
            return 0
        n = len(s)
        res = []
        opr = '+'
        cur_num = 0
        cur_char = ''
        for i in range(n):
            if s[i].isdigit():
                cur_num = cur_num * 10 + ord(s[i]) - ord('0')

            if (not s[i].isdigit() and not s[i].isspace()) or i == n - 1:
                if opr == '-':
                    res.append(-cur_num)
                elif opr == '+':
                    res.append(cur_num)
                elif opr == '*':
                    res.append(res.pop() * cur_num)
                elif opr == '/':
                    res.append(int(res.pop() / cur_num))
                opr = s[i]
                cur_num = 0

        return int(sum(res))
