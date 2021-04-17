# https://leetcode.com/problems/find-leaves-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Runtime: 24 ms, faster than 96.09% of Python3 online submissions for Find Leaves of Binary Tree.
# Memory Usage: 14.1 MB, less than 94.93% of Python3 online submissions for Find Leaves of Binary Tree.
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        def dfs(node, par = None):
            if node:
                node.par = par
                dfs(node.left, node)
                dfs(node.right, node)

        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield from inorder(node.right)
                yield node

        dfs(root)
        res = []
        queue = [node for node in inorder(root) if node and node.left is None and node.right is None]
        while queue:
            tmp = []
            size = len(queue)
            for i in range(size):
                head = queue.pop(0)
                tmp.append(head.val)
                par = head.par
                if par is None:
                    # Found the root, exit condition
                    res.append([head.val])
                    return res

                if head == par.left:
                    par.left = None

                if head == par.right:
                    par.right = None

                if par.left is None and par.right is None:
                    queue.append(par)

            res.append(tmp)

