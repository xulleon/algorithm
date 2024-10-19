# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
# Runtime: 64 ms, faster than 25.26% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Solution 1
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
# Memory Usage: 16.9 MB, less than 15.72% of Python3 online submissions for Binary Tree Zigzag Level Order Traversal.
from collections import deque, defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque([root])
        res = []
        dirct = 1
        while queue:
            grp = []
            size = len(queue)
            for i in range(size):
                head = queue.popleft()
                if dirct > 0:
                    grp.append(head.val)
                else:
                    grp = [head.val] + grp
                    
                for nbr in [head.left, head.right]:
                    if nbr:
                        queue.append(nbr)
                    
            res.append(grp)
            dirct *= -1
        return res

# Solution 2
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

