# https://leetcode.com/problems/moving-average-from-data-stream/
class MovingAverage:

    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.size = size
        self.pointer = 0
        self.stack = []


    def next(self, val: int) -> float:
        self.stack.append(val)
        new_pointer, end = self.pointer, self.pointer + self.size
        if len(self.stack) < self.size:
            # if the window is too big, shrink to the stack size
            end = len(self.stack)
        else:
            # if the window >= self.size, the move the pointer
            self.pointer += 1

        return sum(self.stack[new_pointer:end]) / (end - new_pointer)
