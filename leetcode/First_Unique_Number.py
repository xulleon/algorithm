# https://leetcode.com/problems/first-unique-number/
from collections import defaultdict
class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.dp = defaultdict(int)
        for num in nums:
            self.dp[num] += 1
        self.point = 0

    def showFirstUnique(self) -> int:
        n = len(self.nums)
        while self.point < n:
            if self.dp[self.nums[self.point]] == 1:
                return self.nums[self.point]
            else:
                self.point += 1
                continue
        return -1

    def add(self, value: int) -> None:
        if self.dp[value] == 0:
            self.nums.append(value)
        self.dp[value] += 1
