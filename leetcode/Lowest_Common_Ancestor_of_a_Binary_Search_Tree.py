# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.dc(root, p, q)

    def dc(self, node, node1, node2):
        if node is None or node1 is None or node2 is None:
            return None

        if node1 is node or node2 is node:
            return node

        left = self.dc(node.left, node1, node2)
        right = self.dc(node.right, node1, node2)

        if left and right:
            return node

        if not left and not right:
            return None

        if not left:
            return right

        if not right:
            return left

        return None

