#Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""
The reason why it uses preorder  traverse, was because count depth starting from the top. knowing the top as depth one, then check left depth, and them right.

Traverse means to use a global variable to carry the expected value.  it has to start from a known node which is root. From root, it traverse to its left and right, and each layer.

when it is at root, it needs to calculate its depth by compare the global variable depth with current node depth as a binary may not be balanced.
        self.depth = max(self.depth, cur_depth)
        self.dfs(node.left, cur_depth + 1)
        self.dfs(node.right, cur_depth + 1)
"""
Divided Conquer
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Devided & Conquer
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        return max(self.maxDepth(root.left)+1, self.maxDepth(root.right) + 1)
#Recursive
class Solution:
    depth = 0
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        self.dfs(root, 1)
        return self.depth

    def dfs(self, root, cur_depth):
        if root is None:
            return cur_depth

        self.depth = max(self.depth, cur_depth)
        self.dfs(root.left, cur_depth + 1)
        self.dfs(root.right, cur_depth + 1)
