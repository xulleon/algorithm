# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
# Solution One: use DFS to reconstruct the tree, add parent and target as top node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import defaultdict
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        # find the node, do bfs to get all k nodes below it

        # get its parent and check if it is right or left,
        # get the parent node and find the k-1 distance from
        # the parent node. and so on
        # reconstruct the tree with target as top node. insert a parent node.
        def dfs(node, parent = None):
            if node:
                node.parent = parent
                dfs(node.left, node)
                dfs(node.right, node)
        if K == 0:
            return [target.val]

        dfs(root)
        res = []
        visited = defaultdict(bool)
        queue = deque([target])
        visited[target] = True
        count = 0
        while queue:
            if count == K:
                return res

            size = len(queue)
            count += 1
            for _ in range(size):
                head = queue.popleft()
                for nbr in (head.left, head.right, head.parent):
                    if nbr is None:
                        continue
                    if visited[nbr]:
                        continue
                    if count == K:
                        res.append(nbr.val)
                    queue.append(nbr)
                    visited[nbr] = True

        return []

# Solution Two> same method, but better implementation.

