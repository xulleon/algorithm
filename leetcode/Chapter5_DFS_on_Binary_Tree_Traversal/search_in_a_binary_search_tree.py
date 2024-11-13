# https://leetcode.com/problems/search-in-a-binary-search-tree/

# Divide & Conque
# Runtime: 73 ms, faster than 98.47% of Python3 online submissions for Search in a Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if val == root.val:
            return root

        return self.searchBST(root.left, val) if val < root.val else self.searchBST(root.right, val)


# Traversal Solution One: Iteration One
# Runtime: 131 ms, faster than 35.08% of Python3 online submissions for Search in a Binary Search Tree.
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None

        paths = []
        if val == root.val:
            return root
        elif val > root.val:
            root = root.right
        else:
            root = root.left

        while root:
            paths.append(root)
            root = root.left

        while paths:
            node = paths[-1]
            if node.val == val:
                return node

            if node.right:
                node = node.right
                while node:
                    paths.append(node)
                    node = node.left
            else:
                node = paths.pop()
                while paths and paths[-1].right == node:
                    node = paths.pop()
        return None


# Traverdal Solution Two: Iteration Two
# Runtime: 78 ms, faster than 95.55% of Python3 online submissions for Search in a Binary Search Tree.
# Traverdal Solution One
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return None
        if val == root.val:
            return root
        elif val < root.val:
            root = root.left
        else:
            root = root.right
        if root == None:
            return None

        res, path = [], []
        while path or root:
            while root:
                path.append(root)
                root = root.left

            root = path.pop()
            if root.val == val:
                return root

            root = root.right


# Traversal Solution Three: Preorder
# Runtime: 104 ms, faster than 67.43% of Python3 online submissions for Search in a Binary Search Tree.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        self.res = None
        if not root:
            return

        self.dfs(root, val, False)
        return self.res

    def dfs(self, root, val, found):
        if root == None:
            Return

        # This is how to stop further search if val is found
        if found:
            return

        if root.val == val:
            self.res = root
            #self.found = True
            found = True
            return

        self.dfs(root.left, val, found)
        self.dfs(root.right, val, found)

