# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Solutions one, two pointers. Better performance
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        start, end = 0, len(numbers) - 1
        while start < end:
            if numbers[start] + numbers[end] == target:
                return [start + 1, end + 1]
            elif numbers[start] + numbers[end] > target:
                end -= 1
            else:
                start += 1

        return [-1, -1]

# Solution two: use binary search
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = len(numbers)
        if n == 0:
            return []

        for i in range(n - 1):
            newt = target - numbers[i]
            j = self.helper(numbers[i + 1:], newt)
            print(f'{i} - {j}')
            if j == -1:
                continue

            return [i+1, i+j+2]

    def helper(self, nums, target):

        start, end = 0, len(nums) - 1
        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid
            else:
                start = mid

        if nums[start] == target:
            return start

#         if nums[end] == target:
#             return end

#         return -1
