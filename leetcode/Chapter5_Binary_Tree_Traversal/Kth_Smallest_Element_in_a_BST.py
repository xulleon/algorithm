# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Traversal Solution Two: Iteration One
# Runtime: 67 ms, faster than 73.24% of Python3 online submissions for Kth Smallest Element in a BST.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None:
            return None

        lower_res = []
        path = []
        while root:
            path.append(root)
            root = root.left

        cnt = 1
        while path:
            node = path[-1]
            if cnt == k:
                return node.val
            if node.right:
                node = node.right
                while node:
                    path.append(node)
                    node = node.left
            else:
                node = path.pop()
                while path and path[-1].right == node:
                    node = path.pop()

            cnt += 1

# Traversal Solution Three: Iteration Two
# Runtime: 96 ms, faster than 27.72% of Python3 online submissions for Kth Smallest Element in a BST.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root == None:
            return None

        path = []
        cnt = 1
        while path or root:
            while root:
                path.append(root)
                root = root.left

            root = path.pop()
            if cnt == k:
                return root.val
            root = root.right
            cnt += 1





# Traversal Solution Four: inorder with heapq
# Runtime: 87 ms, faster than 42.07% of Python3 online submissions for Kth Smallest Element in a BST.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        from heapq import heappop, heappush
        if root is None:
            return None

        def dfs(root):
            if root is None:
                return
            dfs(root.left)
            heappush(res, -root.val)
            if len(res) > k:
                heappop(res)
            dfs(root.right)

        res = []
        dfs(root)
        if len(res) == k:
            return -heappop(res)
        return None

