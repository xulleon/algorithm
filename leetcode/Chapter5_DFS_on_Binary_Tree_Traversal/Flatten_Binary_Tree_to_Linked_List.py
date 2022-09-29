# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Devide and Conque
# Runtime: 37 ms, faster than 96.21% of Python3 online submissions for Flatten Binary Tree to Linked List.
class Solution:
    lastnode = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.dfs(root)

    def dfs(self, root):
        if root == None:
            return None
        # left_lastnode is the last node in root.left
        left_lastnode = self.dfs(root.left)

        # right_lastnode is the last node in root.right
        right_lastnode = self.dfs(root.right)

        if left_lastnode:
            if root.right:
                left_lastnode.right = root.right

            root.right = root.left
            root.left = None

        # in terms of last node of the root. the order shoudl be
        # right_lastnode, left_lastnode, root
        if right_lastnode:
            return right_lastnode

        if left_lastnode:
            return left_lastnode

        return root

# Traversal
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Traversal
# difference from divide and conque, traversal starts from top.
# This time preorder is used
# lets say we have root, root.left, root.right. it means that root is the lastnode of root.left and root.left is the lastnode of root.right. we do
# 1) save root.right in a temp variable called right
# 2) assume that after both self.flattern(root.left) and flattern(right), both root.left and root.right become flatterned.
# 3) root.right = root.left (remember that root.right was assigned to a variable right.)
# 4) root.left = None
# 5) if self.lastnode. block is the next time space of the following preorder process. it means when self.lastnode is root, then "the root" is either root.left or root.right.
class Solution:
    lastnode = None
    def flatten(self, root: Optional[TreeNode]) -> None:
        if root == None:
            return

        if self.lastnode:
            self.lastnode.right = root
            self.lastnode.left = None

        self.lastnode = root
        # since self.lastnode.right = root, we need right to remember root.right
        right = root.right
        self.flatten(root.left)
        self.flatten(right)
