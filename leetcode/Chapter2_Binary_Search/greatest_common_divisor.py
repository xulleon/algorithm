# https://www.lintcode.com/problem/845/
"""
THIS NEEDS TO BE REMEMBERED!!!
# 辗转相除法， 又名欧几里德算法， 是求最大公约数的一种方法。它的具体做法是：用较大的数除以较小的数，
# 再用除数除以出现的余数（第一余数），再用第一余数除以出现的余数（第二余数），如此反复，直到最后余数是
# 0为止。如果是求两个数的最大公约数，那么最后的除数就是这两个数的最大公约数。
"""

"""
Let’s take a pair of numbers, (big, small) = (16, 12)
Step 1: big%small: 16/12 = (12 + 4) / 12 = 1 + 4/12 or 16 = 12 + 4%12  (12, 4)
Step 2: big%small: 12/4 = ( 3 x 4+ 0)/4 = 3 + 0 or 12 = 3x4 + 0%4 -> (4, 0)
Step 3: since small is 0, then big is the greatest common devisor

From step2, we know that 4 can divide both 12 and 4, from step 1, we know that 4 can divide both 16, which is (12 + 4) and 12, which indicates at step 2

Every time, it narrows down the mod until the mod is 0, otherwise, it will not get the common divisor.

In other word, when get the small to 0, it means (current pair is (12, 4))
•	it is the first time that the current small, 4 can fully divide current big, 12.

 The previous pair is (16, 12), the small, 12 is the current big, 12. The previous big, 16 -> (12 + 4), has two parts,
•	first part, i.e. 12 can be fully divided by current big, 12
•	second part, the mod, i.e. 4, can be divided by the current small, 4
since it is the first time 4 can fully divide both 16 and 12, therefore, it is the greatest common divisor!!
"""

def gcd(big, small):
    if small != 0:
        return gcd(small, big % small)
    else:
        return big

