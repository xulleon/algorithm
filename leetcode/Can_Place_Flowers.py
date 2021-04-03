# https://leetcode.com/problems/can-place-flowers/
class Solution:
    # Solution One: traverse, Runtime: 164 ms, faster than 71.94%
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        for i in range(m):
            if (i == 0 or flowerbed[i-1] == 0) and flowerbed[i] == 0 and (i == m - 1 or flowerbed[i+1] == 0):
                n -= 1
                flowerbed[i] = 1
            if n < 1:
                return True
        return False

    # Solution Two: Recurive call faster than 5%
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0:
            return True

        if len(flowerbed) < 2:
            if flowerbed == [] or flowerbed == [1]:
                return False

            if flowerbed == [0]:
                return False if n > 1 else True

        if flowerbed[0] == 1 and flowerbed[1] == 0:
            # [1,0,....]
            return self.canPlaceFlowers(flowerbed[2:], n)

        if flowerbed[0] == 0 and flowerbed[1] == 1:
            # [0,1,....]
            return self.canPlaceFlowers(flowerbed[1:], n)

        # [0, 0, ...]
        return self.canPlaceFlowers(flowerbed[2:], n - 1)

