# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Divice & Conque
# Runtime: 56 ms, faster than 66.31% of Python3 online submissions for Closest Binary Search Tree Value.
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root == None:
            return None

        lowerB = self.lower_bound(root, target)
        higherB = self.higher_bound(root, target)

        if lowerB and higherB:
            return lowerB.val if target - lowerB.val <= higherB.val - target else higherB.val

        if lowerB:
            return lowerB.val

        if higherB:
            return higherB.val

        return None

    def higher_bound(self, root, target):
        if root == None:
            return None

        if root.val == target:
            return root

        if target > root.val:
            return self.higher_bound(root.right, target)

        node = self.higher_bound(root.left, target)

        return node if node else root

    def lower_bound(self, root, target):
        if root == None:
            return None

        if root.val == target:
            return root

        if target <= root.val:
            return self.lower_bound(root.left, target)

        node = self.lower_bound(root.right, target)
        return node if node else root


# Traversal Solution One:
# Runtime: 56 ms, faster than 66.37% of Python3 online submissions for Closest Binary Search Tree Value.
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:

        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []

        return min(inorder(root), key = lambda x: abs(target - x))

# Traversal: Iteration One
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root == None:
            return None

        closest = root.val
        while root:
            closest = min(closest, root.val, key = lambda x: abs(target - x))
            root = root.left if target < root.val else root.right
        return closest


# Traversal: Iteration Two
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root == None:
            return None

        if target == root.val:
            return root
        elif target < root.val:
            root = root.left
        else:
            root = root.right


        path, lowest = [], float('-inf')
        while path or root:
            while root:
                path.append(root)
                root = root.left

                root = path.pop()
                if lowest <= target < root.val:
                    return min(lowest, root.val, key = lambda x: abs(target - x))

                lowest = root.val
                root = root.right
        return lowest



# Iteration Three
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root == None:
            return None

        lowest, stack = float("-inf"), []

        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack[-1]
            if lowest <= target < node.val:
                return min(lowest, node.val, key = lambda x: abs(target - x))

            lowest = node.val

            if node.right:
                node = node.right
                while node:
                    stack.append(node)
                    node = node.left
            else:
                node = stack.pop()
                while stack and stack[-1].right == node:
                    node = stack.pop()

        return lowest
