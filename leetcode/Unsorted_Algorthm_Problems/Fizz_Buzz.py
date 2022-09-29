# https://leetcode.com/problems/fizz-buzz/
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []

        for i in range(1, n+1):
            mold3 = i % 3 == 0
            mold5 = i % 5 == 0
            if mold3 and mold5:
                res.append('FizzBuzz')
            elif mold3:
                res.append('Fizz')
            elif mold5:
                res.append('Buzz')
            else:
                res.append(str(i))

        return res
