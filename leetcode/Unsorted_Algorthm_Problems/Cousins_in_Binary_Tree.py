# https://leetcode.com/problems/cousins-in-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dp = {}
        if root is None:
            return False

        queue = [root]
        if root.val in [x, y]:
            dp[root.val] = [None, 0]
        level = 0
        while queue:
            size = len(queue)
            level += 1
            for _ in range(size):
                head = queue.pop(0)
                for child in [head.left, head.right]:
                    if child is None:
                        continue

                    if child.val in [x, y]:
                        dp[child.val] = [head.val, level]
                    queue.append(child)

        return dp[x][0] != dp[y][0] and dp[x][1] == dp[y][1]

