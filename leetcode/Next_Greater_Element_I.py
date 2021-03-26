class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        n = len(nums2)
        for x in nums1:
            index = nums2.index(x)
            val = -1
            while index < n - 1:
                index += 1
                if nums2[index] > x:
                    val = nums2[index]
                    break
            res.append(val)

        return res
