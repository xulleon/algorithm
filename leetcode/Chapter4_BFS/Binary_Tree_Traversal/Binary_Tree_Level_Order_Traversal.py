# https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if root == None:
            return res

        queue = [root]
        while queue:
            grp = []
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                grp.append(node.val)
                for nbr in [node.left, node.right]:
                    if not nbr:
                        continue

                    queue.append(nbr)
            res.append(grp)

        return res

# Another version
# Runtime: 3 ms, faster than 100.00% of Python3 online submissions for Binary Tree Level Order Traversal.
# Memory Usage: 17.3 MB, less than 15.21% of Python3 online submissions for Binary Tree Level Order Traversal.
from collections import defaultdict, deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        
        queue = deque([root])
        visited = defaultdict(bool)
        visited[root] = True
        res = []
        while queue:
            level = []
            size = len(queue)
            for _ in range(size):
                head = queue.popleft()
                level.append(head.val)
                for child in [head.left, head.right]:
                    if child is not None and not visited[child]:
                        queue.append(child)
                        visited[child] = True
            res.append(level)
                        
        return res
