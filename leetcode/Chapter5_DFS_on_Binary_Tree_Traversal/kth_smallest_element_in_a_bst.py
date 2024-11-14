# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Traversal Solution One: Iteration One
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

# Morris Algorithm
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 20.2 MB, less than 21.29% of Python3 online submissions for Kth Smallest Element in a BST.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None or k == 0:
            return
        
        stack = []
        while root:
            if root.left:
                cur = root.left
                while cur.right and cur.right != root:
                    cur = cur.right
                    
                if cur.right == root:
                    cur.right = None
                    k -= 1
                    if k == 0:
                        return root.val
                    root = root.right
                    
                else:
                    cur.right = root
                    root = root.left
            else:
                k -= 1
                if k == 0:
                    return root.val
                root = root.right

# None Recursion
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 20.2 MB, less than 21.29% of Python3 online submissions for Kth Smallest Element in a BST.
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None or k == 0:
            return None
        res = []
        def inorder(root, k):
            if root is None:
                return 
            
            inorder(root.left, k)
            res.append(root.val)
            if len(res) >= k:
                return 
            
            inorder(root.right, k)
            
        inorder(root, k)
        return res[k-1]

# None Recursion
# Runtime: 0 ms, faster than 100.00% of Python3 online submissions for Kth Smallest Element in a BST.
# Memory Usage: 20.1 MB, less than 22.22% of Python3 online submissions for Kth Smallest Element in a BST.
# None Recursion
class Solution:
    cnt = 0
    node = None
    res = []
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return None
        
        self.kthSmallest(root.left, k)
        self.cnt += 1
        if k == self.cnt:
            self.node = root.Val
        if self.cnt >= k:
            # This is needed 
            return self.node

        self.kthSmallest(root.right, k)
        return self.node

