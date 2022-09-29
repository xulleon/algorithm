# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
# Runtime: 63 ms, faster than 37.52% of Python3 online submissions for Binary Tree Level Order Traversal II.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import deque
        res = []
        if root == None:
            return res

        queue = deque([root])
        while queue:
            size = len(queue)
            sublist = []
            for _ in range(size):
                node = queue.popleft()
                if not node:
                    continue

                sublist.append(node.val)
                for nbr in [node.left, node.right]:
                    if not nbr:
                        continue
                    queue.append(nbr)

            res = [sublist] + res
        return res

