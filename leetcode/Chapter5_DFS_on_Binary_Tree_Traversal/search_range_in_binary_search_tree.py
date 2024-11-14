# https://www.lintcode.com/problem/11/
# 83 ms time cost· 7.88 MB memory cost· Your submission beats 76.00 % Submissions
# 3 algorithms are implemented. traversal, morris, and non-recursion.
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
    @param root: param root: The root of the binary search tree
    @param k1: An integer
    @param k2: An integer
    @return: return: Return all keys that k1<=key<=k2 in ascending order
    """
    results = []
    def search_range(self, root: TreeNode, k1: int, k2: int) -> List[int]:
        # write your code here
        if root is None:
            return []
        results = []
        # self.inorder(root, k1, k2, results)
        # self.traversal(root, k1, k2, results)
        self.traversal(root, k1, k2, results)
        return results

    def inorder(self, node, k1, k2, results):
        if node is None:
            return results

        self.inorder(node.left, k1, k2, results)
        if k1 <= node.val <= k2:
            results.append(node.val)

        if node.val <= k2:
            self.inorder(node.right, k1, k2, results)

    def traversal(self, node, k1, k2, results):
        if node is None:
            return results
        stack = []
        while node:
            stack.append(node)
            node = node.left

        while len(stack) > 0:
            node = stack[-1]
            if k1 <= node.val <= k2:
                results.append(node.val)

            if node.val > k2:
                return results

            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
                while len(stack) > 0 and stack[-1].right == node:
                    node = stack.pop()

        return results

    def morris(self, node, k1, k2, results):
        if node is None:
            return results

        while node:
            if node.left:
                cur = node.left
                while cur.right and cur.right != node:
                    cur = cur.right

                if cur.right == node:
                    cur.right = None
                    if k1<= node.val <= k2:
                        results.append(node.val)
                    if node.val > k2:
                        return results
                    node = node.right
                else:
                    cur.right = node
                    node = node.left
            else:
                if k1<= node.val <= k2:
                    results.append(node.val)
                if node.val > k2:
                    return results
                node = node.right
