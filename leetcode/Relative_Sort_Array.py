# https://leetcode.com/problems/relative-sort-array/
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        n = len(arr1)
        extra = []
        for i in range(n-1, -1, -1):
            if arr1[i] not in arr2:
                extra.append(arr1[i])
                arr1.pop(i)
                continue
        extra.sort()
        # Now arr1 only includes integers in arr2 and
        # extra holds integers not in arr2
        arr2index = {v: ind for ind, v in enumerate(arr2)}
        arr2val = {ind: v for ind, v in enumerate(arr2)}
        # change value to arr2 index as index holds actural order
        arr1 = [arr2index[k] for k in arr1]
        arr1.sort()
        # translate indices back to the orignal values
        arr1 = [arr2val[k] for k in arr1]
        arr1.extend(extra)
        return arr1
