# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive
class Solution:
    # Use a global value
    found = False
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        results = []
        self.dfs(root, targetSum)
        return self.found


    def dfs(self, root, target):
        if root is None:
            return

        if root.left is None and root.right is None:
            # it is a leaf
            if target - root.val == 0:
                self.found = True
                return True

        if not self.found:
            # Typical DFS Template
            target -= root.val
            self.dfs(root.left, target)
            self.dfs(root.right, target)
            target += root.val




# Divided & Conque
# class Solution:
#     def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
#         return self.dfs(root, targetSum)
#         if root is None:
#             return 0

#         return self.dfs(root, targetSum)

#     def dfs(self, root, target):

#         if root.left is None and root.right is None and target - root.val == 0:
#             return True
#         # Below is the typical Divided & Conque template
#         if root.left:
#             if self.dfs(root.left, target - root.val):
#                 return True

#         if root.right:
#             if self.dfs(root.right, target - root.val):
#                 return True
