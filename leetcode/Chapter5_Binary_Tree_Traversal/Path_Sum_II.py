# https://leetcode.com/problems/path-sum-ii/submissions/
#Divided & Conque
# Runtime: 55 ms, faster than 79.14% of Python3 online submissions for Path Sum II.
#Runtime: 55 ms, faster than 79.14% of Python3 online submissions for Path Sum II.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return self.dfs(root, targetSum, 0)

    def dfs(self, root, target, level):
        # level is used to know where the top root is.
        paths = []
        if root is None:
            return paths

        # left_paths has >1 paths, same applies to right_paths.
        left_paths = self.dfs(root.left, target - root.val, level + 1)
        right_paths = self.dfs(root.right, target - root.val, level + 1)

        if not root.left and not root.right:
            # Leaf: a special treatment for a leaf
            if target == root.val:
                paths.append([root.val])

        for path in left_paths:
            paths.append([root.val] + path)

        for path in right_paths:
            paths.append([root.val] + path)

        if level == 0:
            # when it is top root, it is time to return paths.
            return paths
        return paths

# Recursive
# Runtime: 83 ms, faster than 28.24% of Python3 online submissions for Path Sum II.
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        results = []
        self.dfs(root, targetSum, [], results)
        return results

    def dfs(self, root, target, subsets, results):
        if root is None:
            return
        if root.left is None and root.right is None:
            if target == root.val:
                # when to the leaf, it is tht tiem to make decision if it meets the criteria.
                subsets.append(root.val)
                results.append(subsets)
            return
        # Recursive is to collect nodes from top root to the leave
        subsets.append(root.val)
        target -= root.val
        self.dfs(root.left, target, subsets[:], results)
        self.dfs(root.right, target, subsets[:], results)
        subsets.pop()
        target += root.val
