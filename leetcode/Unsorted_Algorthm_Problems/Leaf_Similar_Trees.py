# https://leetcode.com/problems/leaf-similar-trees/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                if node.left is None and node.right is None:
                    yield node.val
                yield from inorder(node.right)

        return list(inorder(root1)) == list(inorder(root2))
