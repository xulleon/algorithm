# https://leetcode.com/problems/increasing-order-search-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution One: use inorder generator to recreate a new tree
#           Runtime: 32 ms, faster than 64.10% of Python3
#.          online submissions for Increasing Order Search Tree.
#           Memory Usage: 14.4 MB, less than 43.07%
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node.val
                yield from inorder(node.right)

        first_node = None
        prev = None
        for val in inorder(root):
            node = TreeNode(val)
            if first_node is None:
                first_node = node

            if prev is not None:
                prev.left = None
                prev.right = node

            prev = node

        return first_node



    # Solution Two: use original tree in inorder recursion.
.    # similar performance.
    class Solution:
    first_node = None
    # last_node is in comparison of current node root.
    # it always come from either left or its parent.
    last_node = None
    def increasingBST(self, root: TreeNode) -> TreeNode:
        if root is None:
            return

        self.increasingBST(root.left)
        if self.first_node is None:
            self.first_node = root

        if self.last_node:
            # for preorder, last_node is
            # always from either left or its parent.
            # to prevent dead cycle, first need to
            # remove last_node from root
            # if this is a preorder, then root.left = None is not needed !!
            root.left = None
            self.last_node.right = root
            self.last_node.left = None

        self.last_node = root
        self.increasingBST(root.right)

        return self.first_node


