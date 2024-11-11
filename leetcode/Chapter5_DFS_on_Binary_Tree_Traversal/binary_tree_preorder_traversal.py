# https://leetcode.com/problems/binary-tree-preorder-traversal/submissions/
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 16.6 MB, less than 20.01% of Python3 online submissions for Binary Tree Preorder Traversal.
#
# Recursion
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        results = []
        self.dfs(root, results)
        return results
    
    def dfs(self, root, results):
        if root is None:
            return
        
        results.append(root.val)
        self.dfs(root.left, results)
        self.dfs(root.right, results)

# Morris Algorithm
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Binary Tree Preorder Traversal.
# Memory Usage: 16.7 MB, less than 21.47% of Python3 online submissions for Binary Tree Preorder Traversal.
# Morris Algorithm
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        
        results = []
        while root:
            if root.left:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right
                    
                if cur.right == root:
                    cur.right = None
                    root = root.right
                else:
                    results.append(root.val)
                    cur.right = root
                    root = root.left
            else:
                results.append(root.val)
                root = root.right
                
        return results
