# https://leetcode.com/problems/binary-tree-inorder-traversal/
# Recursive solution one:
# Runtime: 41 ms, faster than 70.32% of Python3 online submissions for Binary Tree Inorder Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        for node in self.dfs(root):
            res.append(node.val)
        return res

    def dfs(self, root):
        if root:
            yield from self.dfs(root.left)
            yield root
            yield from self.dfs(root.right)

# Recursive Example Two
# Runtime: 43 ms, faster than 64.19% of Python3 online submissions for Binary Tree Inorder Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:

#     def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if root is None:
            return

        self.dfs(root.left, res)
        res.append(root.val)
        self.dfs(root.right, res)

# Iteration
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Iteration One
class Solution:

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res, path = [], []
        while root:
            path.append(root)
            root = root.left

        while path:
            node = path[-1]
            res.append(node.val)

            if node.right:
                node = node.right
                while node:
                    path.append(node)
                    node = node.left
            else:
                node = path.pop()
                while path and path[-1].right == node:
                    node = path.pop()

        return res

# Iteration Two
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        res,  path = [], []
        while path or root:
            while root:
                path.append(root)
                root = root.left

            root = path.pop()
            res.append(root.val)

            root = root.right

        return res

