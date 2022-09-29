# https://leetcode.com/problems/binary-tree-maximum-path-sum/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
"""
Divided & Conque: assume left and right max path sum.
For root: cur_max = root.val + left_sum + right_sum is the max path sum
For root: root.val + max(left_sum, right_sum) is the max path sum from root to the leaf, which maybe in either left or right of the root.
"""
class Solution:
    max_int = float('-inf')
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.dfs(root)
        return self.max_int

    def dfs(self, root):
        if root is None:
            return 0

        left_sum = max(self.dfs(root.left), 0)
        right_sum = max(self.dfs(root.right), 0)

        cur_max = root.val + left_sum + right_sum
        self.max_int = max(self.max_int, cur_max)

        return root.val + max(left_sum, right_sum)
