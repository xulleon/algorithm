# https://leetcode.com/problems/binary-tree-postorder-traversal/submissions/
# Morris algorithm
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 16.6 MB, less than 20.69% of Python3 online submissions for Binary Tree Postorder Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        results = []
        while root:
            if root.right:
                cur = root.right
                while cur.left and cur.left != root:
                    cur = cur.left
                    
                if cur.left == root:
                    cur.left = None
                    root = root.left
                else:
                    results.append(root.val)
                    cur.left = root
                    root = root.right
            else:
                results.append(root.val)
                root = root.left
 
        return results[::-1]

# recursion
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Binary Tree Postorder Traversal.
# Memory Usage: 16.6 MB, less than 56.23% of Python3 online submissions for Binary Tree Postorder Traversal.
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        results = []
        self.dfs(root, results)
        return results
    
    def dfs(self, root, results):
        if root is None:
            return
        
        self.dfs(root.left, results)
        self.dfs(root.right, results)
        results.append(root.val)
