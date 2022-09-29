# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Runtime: 64 ms, faster than 25.26% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root == None:
            return []

        from collections import deque
        queue = deque([root])
        left2right = False
        while queue:
            size = len(queue)
            sublist = []
            for _ in range(size):
                node = queue.popleft()
                if not node:
                    continue

                sublist.append(node.val)
                nodes = [node.left, node.right]
                for nbr in nodes:
                    if not nbr:
                        continue
                    queue.append(nbr)

            if left2right:
                sublist = sublist[::-1]

            res.append(sublist)
            left2right = not left2right

        return res

