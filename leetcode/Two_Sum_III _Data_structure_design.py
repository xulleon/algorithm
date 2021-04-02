# https://leetcode.com/problems/two-sum-iii-data-structure-design/
class TwoSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.numbers = {}


    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number in self.numbers:
            self.numbers[number] += 1
        else:
            self.numbers[number] = 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for number in self.numbers.keys():
            number1 = value - number
            if number1 != number:
                if number1 in self.numbers:
                    return True
            else:
                if self.numbers[number] > 1:
                    return True
        return False
