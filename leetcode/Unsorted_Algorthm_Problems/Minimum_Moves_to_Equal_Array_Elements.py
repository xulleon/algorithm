# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        '''
        an exampe of [1,3,2], sorted to [1, 2, 3]. nums[0] = 1, nums[1] = 2, nums[2] = 3
        1) find the diff between the max and min, which is nums[2] - nums[0] = 3 -1 = 2
        2) moves += diff, -> 2. all some update all others except the max itself.
        3) now the max is 4 ( 2 + num[1]), the min is 3 (num[0] + 2).,
           diff is 4 -3 = (nums[1] + 2) - (nums[0] + 2) = 1
        4) second moves is moves += diff, -> 3
        5) update the result except the max, which is the middle one, then all of them are 4


           (1)                                  (2)                                 (3)
                                             |                                |. |. |
            |                             |  |  |                             |. |. |
          | |   add 2 on index 0 and 1 -> |  |  |  add 1 on index 0 and 2 ->  |  |. |
        | |.|                             |  |  |                             |. |. |

        '''
        n = len(nums)
        nums.sort()
        count = 0
        for i in range(n):
            count += nums[i] - nums[0]

        return count
