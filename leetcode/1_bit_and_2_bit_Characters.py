# https://leetcode.com/problems/1-bit-and-2-bit-characters/
class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits) == 0:
            return False

        if len(bits) == 1:
            return bits[0] == 0
        # len(bits) > 1
        if bits[0] == 1:
            # next digit must be 0 or one if len(bits) > 1
            return self.isOneBitCharacter(bits[2:])
        # list starts with 0 at index 0
        return self.isOneBitCharacter(bits[1:])
