# https://www.lintcode.com/problem/144/record
# 121 ms time cost 6.92 MB memory cost. Your submission beats 11.60 % Submissions
from typing import (
    List,
)

class Solution:
    """
    @param a: An integer array.
    @return: nothing
    """
    def rerange(self, a: List[int]):
        # write your code here
        n = len(a)
        if n < 3:
            return a

        # there is a scenario when the total is odd 
        # number, [-1,1,1], we must set the first 
        # number to be 1, therefore the result shold 
        # be [1,-1,1], same apply to [1,-1,-1]. The 
        # we need to put negative number at index 0 
        # to make it [-1,1,-1]
        # find the first index for positive and negative ints
        if n % 2 == 1:
            pp, np = -1, -1
            p_cnt, n_cnt = 0, 0
            for i in range(n):
                if a[i] >= 0:
                    if pp == -1:
                        pp = i
                    p_cnt += 1
                else:
                    if np == -1:
                        np = i
                    n_cnt += 1

            if p_cnt > n_cnt:
                # if more positive ints, the swap ints to make the first one as positive. i.e. [-1, 1, 1]
                if a[0] < 0:
                    a[pp], a[0] = a[0], a[pp]
            else:
                # i.e. [1, -1,-1]
                if a[0] > 0:
                    a[np], a[0] = a[0], a[np]

        p1, p2 = 0, 1
        while p2 < n:
            while p2 < n and a[p1] * a[p2] < 0:
                p1 += 1
                p2 += 1
            
            if p2 >= n:
                break

            ptr = p2 + 1
            while ptr < n and a[p1] * a[ptr] >= 0:
                ptr += 1

            if ptr >= n:
                break

            a[p2], a[ptr] = a[ptr], a[p2]

        return a
