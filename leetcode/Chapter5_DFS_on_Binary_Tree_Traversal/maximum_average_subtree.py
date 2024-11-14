# https://leetcode.com/problems/maximum-average-subtree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Solution 1
# Runtime: 10 ms, faster than 7.61% of Python3 online submissions for Maximum Average Subtree.
# Memory Usage: 19.5 MB, less than 13.45% of Python3 online submissions for Maximum Average Subtree.
# preorder (root, left, right), inorder (left, root, right), postorder (left, right, root)
import sys
class Solution:
    max_avg = -sys.maxsize
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        if root is None:
            return 0
        
        top = self.postorder(root)
        return max(self.max_avg, sum(top)/len(top))
    
    def postorder(self, root):
        if root is None:
            return []
        
        left = self.postorder(root.left)
        right = self.postorder(root.right)
        
        max_avg = sum(left + right + [root.val])/(len(left) + len(right) + 1)
        self.max_avg = max(self.max_avg, max_avg)
        
        return left + right + [root.val]

  # Solution 2
  class Solution:
    def maximumAverageSubtree(self, root: TreeNode) -> float:
        res = []
        self.helper(root, res)
        return max(res)
    
    def helper(self, node, res):
        if node is None:
            return []

        tmp = self.helper(node.left, res) + self.helper(node.right, res) + [node.val]
        res.append(sum(tmp)/len(tmp))
        
        return tmp
