# https://leetcode.com/problems/asteroid-collision/
# Solution One: not good performance, Runtime: 3732 ms, faster than 5.00%
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        pre_asteroids = []
        self.helper(asteroids, pre_asteroids)
        return asteroids

    def helper(self, asteroids, pre_asteroids):
        if asteroids == pre_asteroids:
            return

        pre_asteroids = asteroids[:]
        n = len(asteroids)
        if n < 2:
            return

        for i in range(1, n):
            if (asteroids[i-1] * asteroids[i] > 0) or asteroids[i-1] < 0 and asteroids[i] > 0:
                # same direction or opposite directions, never meet
                continue

            # when two asteroids will colide
            elif abs(asteroids[i-1]) == abs(asteroids[i]):
                for j in range(2):
                    asteroids.pop(i-1)
                break

            elif abs(asteroids[i-1]) > abs(asteroids[i]):
                asteroids.pop(i)
                break
            else:
                asteroids.pop(i-1)
                break

        self.helper(asteroids, pre_asteroids)
# Solution Two: using stack technique, very good performance. 92 ms, faster than 87.85%
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        n = len(asteroids)
        for num in asteroids:
            while len(res) > 0:
                if res[-1] * num > 0 or (res[-1] < 0 and num > 0):
                    res.append(num)
                    break
                elif res[-1] == -num:
                    res.pop()
                    break
                elif abs(res[-1]) < abs(num):
                    res.pop()
                else:
                    break
            else:
                res.append(num)
        return res
