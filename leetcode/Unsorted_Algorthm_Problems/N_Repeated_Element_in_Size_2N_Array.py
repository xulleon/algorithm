# https://leetcode.com/problems/n-repeated-element-in-size-2n-array/
class Solution:
    # use Counter and sort:
    # Runtime: 256 ms, faster than 9.25%
    # Memory Usage: 16.2 MB, less than 5.83%
    def repeatedNTimes(self, A: List[int]) -> int:
        from collections import Counter
        n = len(A) // 2
        print(f'n: {n}')
        res = Counter(A)
        ans = list(res.items())
        print(ans)
        ans.sort(key=lambda grp: grp[1] == n)
        print(ans)
        return ans[-1][0]

    # Solution Two: traverse to find the item
    # Runtime: 224 ms, faster than 23.26%
    # Memory Usage: 15.5 MB, less than 67.26%
    def repeatedNTimes(self, A: List[int]) -> int:
        from collections import defaultdict
        rec = defaultdict(int)
        target = len(A) // 2
        for num in A:
            rec[num] += 1
            if rec[num] == target:
                return num

