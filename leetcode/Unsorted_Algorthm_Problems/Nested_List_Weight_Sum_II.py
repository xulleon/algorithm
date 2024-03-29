#        https://leetcode.com/problems/nested-list-weight-sum-ii/
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        def toList(nestedList):
            if len(nestedList) == 0:
                return
            inttmp = [item.getInteger() for item in nestedList if item.isInteger()]
            res.append(inttmp)
            # got lists in the same level
            listtmp = [item for item in nestedList if not item.isInteger()]
            # merge the same level's list into one list
            listtmp=[item for items in listtmp for item in items.getList()]
            toList(listtmp)

        ans = 0
        res = []
        toList(nestedList)
        for level, vals in enumerate(reversed(res)):
            ans += sum(vals) * (level + 1)

        return ans
