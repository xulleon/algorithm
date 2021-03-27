class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key=lambda grp: (grp[0], grp[1]))
        count = 0
        rest = []
        n = len(intervals)
        for i in range(1, n):
            if intervals[i-1][1] > intervals[i][0]:
                # any one occurs, will disqualify it
                return False
        return True
