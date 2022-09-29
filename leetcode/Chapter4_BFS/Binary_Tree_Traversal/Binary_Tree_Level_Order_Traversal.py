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

