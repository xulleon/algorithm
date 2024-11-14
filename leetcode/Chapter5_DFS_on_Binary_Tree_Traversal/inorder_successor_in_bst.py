# https://leetcode.com/problems/inorder-successor-in-bst/
# Runtime: 59 ms, faster than 25.83% of Python3 online submissions for Inorder Successor in BST.
# Memory Usage: 20.3 MB, less than 92.43% of Python3 online submissions for Inorder Successor in BST.
class Solution:
    found = False
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> Optional[TreeNode]:
        if root is None:
            return None
        
        stack = []
        while root:
            if root.val == p.val:
                if root.right:
                    root = root.right
                    while root:
                        stack.append(root)
                        root = root.left
                else:
                    while len(stack) > 0 and stack[-1].right == root:
                        root = stack.pop()
                return stack[-1] if len(stack) > 0 else None
                
            elif root.val > p.val:
                stack.append(root)
                root = root.left
            else:
                stack.append(root)
                root = root.right
                
        return None
