# https://leetcode.com/problems/shuffle-the-array/
# Solution One: Runtime: 56 ms, faster than 85.93%
class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        res = []
        left, right = 0, n//2
        while right < n:
            res.extend([nums[left], nums[right]])
            left += 1
            right += 1

        return res

# Solution Two: faster than 26%
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        n = len(nums)
        left, right = 0, n // 2
        while right - left > 1:
            # when left next to right, it reaches the end
            nums.insert(left + 1, nums[right])
            nums.pop(right + 1)
            left += 2
            right += 1

        return nums
