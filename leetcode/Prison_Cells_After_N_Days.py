# https://leetcode.com/problems/prison-cells-after-n-days/
class Solution:

    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        times, cycle, dp = 0, -1, {}
        edge1 = True
        if cells[0] == 0 and cells[len(cells) - 1] == 0:
            edge1 = False

        while times < n:
            if tuple(cells) in dp:
                if cycle == -1:
                    # Found 1st repeatitive, record the cycle
                    if edge1:
                        cycle = times - 1
                    else:
                        cycle = times
                    # since it cycles, then directly skip to the last cycle.
                    times = times + cycle * ((n - times) // cycle)
                if times == n:
                    # line 19 will get 29 for n = 29 or 30 with
                    # cycle = 14 and times = 15. since 29, 85, 99
                    # are at the cycle points. it should skip any
                    # further calculation
                    break
                cells = dp[tuple(cells[:])][:]
            else:
                tmp = cells[:]
                for i in range(1, 7):
                    tmp[i] = 1 if cells[i-1] + cells[i+1] in [0, 2] else 0
                tmp[0] = tmp[7] = 0
                dp[tuple(cells[:])] = tmp[:]
                cells = tmp[:]

            times += 1

        return cells

