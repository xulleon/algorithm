# https://www.lintcode.com/problem/376/
# 81 ms time cost· 5.03 MB memory cost· Your submission beats 78.40 % Submissions
from typing import (
    List,
)
from lintcode import (
    TreeNode,
)

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @param target: An integer
    @return: all valid paths
             we will sort your return value in output
    """
    def binary_tree_path_sum(self, root: TreeNode, target: int) -> List[List[int]]:
        # write your code here
        if root is None:
            return []
        results = []
        self.dfs(root, [], target, results)
        return results

    def dfs(self, node, paths, target, results):
        if node is None:
            return []

        if node.left is None and node.right is None:
            if sum(paths) == target - node.val:
                results.append(paths + [node.val])
        self.dfs(node.left, paths + [node.val], target, results)
        self.dfs(node.right, paths + [node.val], target, results)
