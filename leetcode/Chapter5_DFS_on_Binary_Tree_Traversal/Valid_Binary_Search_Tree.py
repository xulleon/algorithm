# Definition for a binary tree node.
# https://leetcode.com/problems/validate-binary-search-tree/submissions/

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class NewResult:
    def __init__(self, isBST):
        self.isBST = isBST
        self.minNode = None
        self.maxNode = None
# DFS Traversal
# Runtime: 45 ms, faster than 95.08% of Python3 online submissions for Validate Binary Search Tree.
class Solution:
    last_node = None
    isValid = True
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # global last_node
        # global isValid
        self.dfs(root)
        return self.isValid

    def dfs(self, root):
        if root is None:
            return

        self.dfs(root.left)
        if self.last_node != None and self.last_node.val >= root.val:
            self.isValid = False
        self.last_node = root

        self.dfs(root.right)


# Divided & Conque
# Runtime: 73 ms, faster than 45.50% of Python3 online submissions for Validate Binary Search Tree.
# class Solution:
#     last_node = None
#     isValid = True
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         return self.dfs(root).isBST

#     def dfs(self, root):
#         if root == None:
#             return NewResult(True)

#         left = self.dfs(root.left)
#         right = self.dfs(root.right)

#         if left.isBST == False or right.isBST == False:
#             return NewResult(False)

#         if left.maxNode != None and left.maxNode.val >= root.val:
#             return NewResult(False)

#         if right.minNode != None and right.minNode.val <= root.val:
#             return NewResult(False)

#         new_result = NewResult(True)
#         new_result.maxNode = right.maxNode if right.maxNode != None else root
#         new_result.minNode = left.minNode if left.minNode != None else root

#         return new_result
