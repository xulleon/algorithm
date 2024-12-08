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

# Solution 2
# 101 ms time cost· 6.91 MB memory cost· Your submission beats 98.40 % Submissions
'''
The key to resolve the problem by
1)	Use partial quick sort to separate positives and negatives
2)	 using the following scenario to figure out the starting pos and neg index.
•	Equal pos and neg [-1,-2,-3,4,5,6], [[-1,-2,-3,-4,5,6,7,8]
•	More pos [-1,-2,4,5,6], [[-1,-2,-3,5,6,7,8]
•	More neg [-1,-2,-3,4,5], [[-1,-2,-3,-4,5,6,7]

'''
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

        # reorg the list by negative first then positive using partial quicksort
        pl, pr = 0, n - 1
        while pl <= pr:
            while pl < pr and a[pl] < 0:
                pl += 1

            while pl <= pr and a[pr] > 0:
                pr -= 1

            if pl <= pr:
                a[pl], a[pr] = a[pr], a[pl]
                pl += 1
                pr -= 1

        pos = pl
        pos_cnt = n - pl
        neg_cnt = pl

        # same number of positives and negatives
        if pos_cnt == neg_cnt:
            # below can be simplified as 
            # “self.flip(a, 0, pos + (pos_cnt+1)%2)”
            if pos_cnt % 2 == 0:
                # start from 1st negative and 2nd positive
                self.flip(a, 0, pos+1)
            else:
                # start from 1st negative and 1st positive
                self.flip(a, 0, pos)
        else:
            if neg_cnt > pos_cnt:
                # more negatives
                # more negatives
                # below can be simplified as 
                # “self.flip(a, 1, pos + neg_cnt % 2)”
                if neg_cnt % 2 == 0:
                    # start from 2nd negative and 1st positive
                    self.flip(a, 1, pos)
                else:
                    # start from 2nd negative and 2nd positive
                    self.flip(a, 1, pos+1)
            else:
                # more positives
                a.reverse()
                # the following can be “self.flip(1, n - pos + pos_cnt%2)”
                if pos_cnt % 2 == 0:
                    # start from 2nd positive and 1st negative
                    self.flip(a, 1, n - pos)
                else:
                    # start from 2nd positive and 2nd negative
                    self.flip(a, 1, n-pos + 1)

        return a

    def flip(self, a, start, end):
        n = len(a)
        while end < n:
            a[start], a[end] = a[end], a[start]
            start += 2
            end += 2




