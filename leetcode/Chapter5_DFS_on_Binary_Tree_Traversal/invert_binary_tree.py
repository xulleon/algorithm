# https://leetcode.com/problems/invert-binary-tree/
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Invert Binary Tree.
# Memory Usage: 16.8 MB, less than 20.23% of Python3 online submissions for Invert Binary Tree.
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        root.right, root.left = root.left, root.right
        return root
                                                                     
