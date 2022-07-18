# https://leetcode.com/problems/regular-expression-matching/submissions/
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i, j = 0, 0
        if len(s) == 0:
            return self.checkempty(p)

        if len(p) == 0:
            return False

        f1, p1 = s[0], p[0]
        if len(p) > 1:
            p2 = p[1]
        else:
            p2 = None

        if p2 and p2 == '*':
            if self.compare(f1, p1):
                return (self.isMatch(s[1:], p) or self.isMatch(s, p[2:]))
            else:
                return self.isMatch(s, p[2:])
        else:
            if self.compare(f1, p1):
                return self.isMatch(s[1:], p[1:])

            else:
                return False
        return True

    def checkempty(self, p):

        if len(p) >= 2:
            if p[1] == '*':
                return self.checkempty(p[2:])
        elif len(p) == 0:
            return True

        else: # len(p) == 1:
            return False


    def compare(self, f1, p1):
        if p1 =='.' or f1 == p1:
            return True

        return False
