# https://leetcode.com/problems/replace-elements-with-greatest-element-on-right-side/
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        print(arr)
        for i in range(len(arr)):
            if i == len(arr) - 1:
                arr[i] = -1
                break
            arr[i] = max(arr[i+1:])

        return arr
