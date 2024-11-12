# Binary Tree Path
# https://leetcode.com/problems/binary-tree-paths/
## Devided & Conque ##
"""
For devided & Conque, it is a post order. therefore left, right then root.
root.left was process first, it will drill down to the leaf at the left side.
leaf is the bottom. that is why, path.append(str(root.val))
then it will tackback all the way to the top root. that is why 
path.append(str(root.val) + '->' + path)

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# divide & conquer
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Binary Tree Paths.
# Memory Usage: 16.7 MB, less than 7.13% of Python3 online submissions for Binary Tree Paths.
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        if root is None:
            return []

        paths = []
        left_paths = self.binaryTreePaths(root.left)

        right_paths = self.binaryTreePaths(root.right)

        if left_paths:
            for path in left_paths:
                paths.append(str(root.val) + '->' + path)

        if right_paths:
            for path in right_paths:
                paths.append(str(root.val) + '->' + path)

        if not (left_paths or right_paths):
            # leaf treatment
            paths.append(str(root.val))

        return paths

## Recursive ##
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Binary Tree Paths.
# Memory Usage: 16.6 MB, less than 72.16% of Python3 online submissions for Binary Tree Paths.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
"""
There might be more than one paths from top root to each leaf. Therefore, it needs to know when the leaf is reached (leaf with left and right nodes as null). Then that is the time to append the path into results. For this any of preorder, inorder and postorder all works.
"""
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        results = []
        self.dfs(root, str(root.val), results)
        return results

    def dfs(self, root, paths, results):
        if root is None:
            # This makes sure that a node with null left or right will got None node.
            return
        # add the path to results when hits a leaf
        if root.left == None and root.right == None:
            results.append(paths)

        if root.left:
            self.dfs(root.left, paths + '->' + str(root.left.val), results)

        if root.right:
            self.dfs(root.right, paths + '->' + str(root.right.val), results)
