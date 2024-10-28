# https://leetcode.com/problems/find-k-closest-elements/
# Runtime: 158 ms, faster than 5.21% of Python3 online submissions for Find K Closest Elements.
# Memory Usage: 18.2 MB, less than 47.44% of Python3 online submissions for Find K Closest Elements.
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        n = len(arr)
        if n == 0:
            return []

        if n < k:
            return []

        left, right = self.helper(arr, x)

        res = []
        for i in range(k):
            if left >= 0 and right < n:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    res = [arr[left]] + res
                    left -= 1
                else:
                    res += [arr[right]]
                    right += 1
            elif left < 0:
                res.append(arr[right])
                right += 1
            else:
                res = [arr[left]] + res
                left -= 1

        #print(res)
        return res        


    def helper(self, nums, target):
        start, end = 0, len(nums) - 1

        while start + 1 < end:
            mid = (start + end) // 2
            if nums[mid] <= target:
                start = mid
            else:
                end = mid

        return (start, end)
