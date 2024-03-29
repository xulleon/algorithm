# https://leetcode.com/problems/design-parking-system/
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.parklots = {1: big, 2: medium, 3: small}


    def addCar(self, carType: int) -> bool:
        if self.parklots[carType] > 0:
            self.parklots[carType] -= 1
            return True
        return False
