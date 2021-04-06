# https://leetcode.com/problems/sum-of-left-leaves/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                if node.left:
                    yield node.left
                yield from inorder(node.right)

        res = [node.val for node in inorder(root) if node.left is None and node.right is None]
        return sum(res)
