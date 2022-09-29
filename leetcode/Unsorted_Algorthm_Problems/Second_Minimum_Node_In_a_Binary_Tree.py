# https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if root is None:
            return -1

        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)
        nodes = set()
        for val in inorder(root):
            nodes.add(val)
        nodes = sorted(nodes)
        return -1 if len(nodes) <= 1 else nodes[1]
