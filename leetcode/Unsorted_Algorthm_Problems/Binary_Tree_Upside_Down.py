# https://leetcode.com/problems/binary-tree-upside-down/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def upsideDownBinaryTree(self, root: TreeNode) -> TreeNode:
        if not root :
            return root

        stk=[root]
        while root.left:
            root=root.left
            stk.append(root)

        while stk:
            curr=stk.pop()
            if stk:
                curr.left=stk[-1].right
                stk[-1].right = None
                stk[-1].left = None
                curr.right=stk[-1]
            else:
                curr.left=None
                curr.right=None
        return root
