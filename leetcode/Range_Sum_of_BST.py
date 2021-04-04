# https://leetcode.com/problems/range-sum-of-bst/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def inorder(node):
            if node:
                if node.val > low:
                    yield from inorder(node.left)

                if node.val < high:
                    yield from inorder(node.right)

                if low <= node.val <= high:
                    yield node.val
        count = 0
        for val in inorder(root):
            count += val
        return count
