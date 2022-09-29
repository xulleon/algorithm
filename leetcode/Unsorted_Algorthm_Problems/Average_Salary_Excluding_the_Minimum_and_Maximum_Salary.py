# https://leetcode.com/problems/average-salary-excluding-the-minimum-and-maximum-salary/
class Solution:
    def average(self, salary: List[int]) -> float:
        if len(salary) < 3:
            return 0

        salary.sort()
        n = len(salary)
        return sum(salary[1:n-1])/(n-2)
