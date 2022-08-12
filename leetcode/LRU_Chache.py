# https://leetcode.com/problems/lru-cache/
from collections import OrderedDict
class LRUCache(OrderedDict):

    def __init__(self, capacity: int):
        self.capacity = capacity


    def get(self, key: int) -> int:
        if key not in self:
            return -1

        self.move_to_end(key)
        return self[key]

    def put(self, key: int, value: int) -> None:
        if key in self:
            self.move_to_end(key)
        else:
            if len(self) >= self.capacity:
                self.popitem(last = False)
        self[key] = value
