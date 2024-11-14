# Traversal
# Runtime: 12 ms, faster than 52.24% of Python3 online submissions for Binary Search Tree Iterator.
# Memory Usage: 24.1 MB, less than 22.72% of Python3 online submissions for Binary Search Tree Iterator.
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.stack = []
    
    
    
    def next(self) -> int:
        while self.root:
            self.stack.append(self.root)
            self.root = self.root.left
            
        self.root = self.stack.pop()
        next_node = self.root
        self.root = self.root.right
        return next_node.val
      
# Traversal, non-recursion and morris
# functions can be uncommented if a specific function is used.
class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.results = []
        
        # self.traversal()
        # self.inorder(self.root)
        self.morris()

    def next(self) -> int:
        return self.results.pop(0)
        
    def hasNext(self) -> bool:
        return len(self.results) > 0
        
    def traversal(self):
        if self.root is None:
            return []
        
        stack = []
        while self.root:
            stack.append(self.root)
            self.root = self.root.left
        while len(stack) > 0:
            self.root = stack[-1]
            self.results.append(self.root.val)
            if self.root.right:
                self.root = self.root.right
                while self.root:
                    stack.append(self.root)
                    self.root = self.root.left
            else:
                self.root = stack.pop()
                while len(stack) > 0 and stack[-1].right == self.root:
                    self.root = stack.pop()     
        return self.results
    
    def inorder(self, root):
        # print('root:', root.val)
        if root is None:
            return []
        
        self.inorder(root.left)
        self.results.append(root.val)
        self.inorder(root.right)
        
    def morris(self):
        node = self.root
        if node is None:
            return []
        
        while node:
            if node.left:
                cur = node.left
                while cur.right and cur.right != node:
                    cur = cur.right
                    
                if cur.right == node:
                    cur.right = None
                    self.results.append(node.val)
                    node = node.right
                    
                else:
                    # cur.right is None
                    cur.right = node
                    node = node.left
            else:
                self.results.append(node.val)
                node = node.right
