# https://leetcode.com/problems/balanced-binary-tree/
# Solution One
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 17.9 MB, less than 13.91% of Python3 online submissions for Balanced Binary Tree.

class Solution:
    NOT_BALANCED = -1
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        return self.get_depth(root) != self.NOT_BALANCED
    
    def get_depth(self, node):
        if node is None:
            return 0
        
        leftdepth = self.get_depth(node.left)
        rightdepth = self.get_depth(node.right)
        
        if leftdepth == self.NOT_BALANCED or rightdepth == self.NOT_BALANCED:
            return self.NOT_BALANCED
        
        if abs(leftdepth - rightdepth)  > 1:
            return self.NOT_BALANCED
        
        return max(leftdepth, rightdepth) + 1

# Solution Two
# Runtime: 10 ms, faster than 15.13% of Python3 online submissions for Balanced Binary Tree.
# Memory Usage: 17.9 MB, less than 34.28% of Python3 online submissions for Balanced Binary Tree.
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        
        leftdepth = self.get_depth(root.left)
        rightdepth = self.get_depth(root.right)
        
        if abs(leftdepth - rightdepth) <= 1:
            if self.isBalanced(root.left) and self.isBalanced(root.right):
                return True
            else:
                return False
        else:
            return False
        
    def get_depth(self, node):
        if node is None:
            return 0
        
        return max(self.get_depth(node.left), self.get_depth(node.right)) + 1
