# https://leetcode.com/problems/sort-array-by-parity/
class Solution:
    # Solution One:
    # Runtime: 80 ms, faster than 58.99% of Python3 online submissions for Sort Array By Parity.
    # Memory Usage: 15 MB, less than 55.95% o
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [k for k in A if k % 2 == 0] + [k for k in A if k % 2 == 1]

    # Solution Two: about 58% . pro is easy, usr customized sort function
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        A.sort(key=lambda x: x % 2)
        return A

    # Solution 3:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if len(A) < 2:
            return A

        index = 0
        i = 0
        n = len(A)
        while i < n:
            if A[i] % 2 == 1:
                A.append(A[i])
                A.pop(i)
            else:
                i += 1
            index += 1
            if index > n - 1:
                break
        return A

