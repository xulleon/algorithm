# https://leetcode.com/problems/closest-binary-search-tree-value-ii/submissions/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
# Solution One
from heapq import heappush, heappop
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def inorder(node):
            if node is None:
                return

            inorder(node.left)
            # use the negative diff to make the greater diff node at the top
            # so that they can be popped out.
            heappush(heap, (-abs(target - node.val), node.val))
            if len(heap) > k:
                heappop(heap)
            inorder(node.right)

        heap = []
        inorder(root)
        return [x for _, x in heap]

# Solution Two
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        def inorder(root):
            if root is None:
                return []

            return inorder(root.left) + [root.val] + inorder(root.right)

        res = inorder(root)
        # use diff of "target - x" to sort those nodes which are closer to target.
        res.sort(key=lambda x: abs(target - x))
        return res[:k]

# Solution Three
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        '''
        The idea is to save all nodes, whose values are less than target in a res list,
        all nodes whose values are greater than target in the generator, by comparing
        the diff to find the answer
        '''
        res = []
        ans = []
        def nav(root):
            if root:
                yield from nav(root.left)
                yield root
                yield from nav(root.right)

        left = -1
        for node in nav(root):
            if node.val < target:
                # save all node whose value is less than target in res list
                res.append(node)
            else:
                # find the first value >= target
                while k > 0:
                    if node and len(res) >= -left:
                        if abs(node.val - target) <= abs(target - res[left].val):
                            ans.append(node.val)
                            k -= 1
                            break
                        else:
                            ans.append(res[left].val)
                            left -= 1
                            k -= 1
                    elif len(res) < -left and node:
                        ans.append(node.val)
                        k -= 1
                        break
                    elif not node and len(res) >= -left:
                        ans.append(res[left].val)
                        left -= 1
                        k -= 1
                    else:
                        # no node left and res has nothing
                        # should not be here
                        return ans

            if k <= 0:
                return ans

        # when no node left, all node value less than target.
        while k > 0:
            ans.append(res[left].val)
            left -= 1
            k -= 1
        return ans

# Solution Four
class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        """
        This requires to really understand how to iterate BST.
        :param root:
        :param target:
        :param k:
        :return:
        """

        results = []
        if not root or target is None or k == 0:
            return results

        lowerstack = self.get_stack(root, target)
        upperstack = lowerstack[:]

        if target < lowerstack[-1].val:
            self.movedown(lowerstack)
        elif target > upperstack[-1].val:
            self.moveup(upperstack)

        for _ in range(k):
            if lowerstack and upperstack:
                if target - lowerstack[-1].val <= upperstack[-1].val - target:
                    results.append(lowerstack[-1].val)
                    self.movedown(lowerstack)
                else:
                    results.append(upperstack[-1].val)
                    self.moveup(upperstack)
            elif lowerstack:
                results.append(lowerstack[-1].val)
                self.movedown(lowerstack)
            elif upperstack:
                results.append(upperstack[-1].val)
                self.movepwdup(upperstack[-1])
        return results

    def movedown(self, stack):
        node = stack[-1]
        if node.left:
            node = node.left
            while node:
                stack.append(stack)
                node = node.right
            return
        else:
            node = stack.pop()
            while stack and stack[-1].left == node:
                node = stack.pop()

    def moveup(self, stack):
        node = stack[-1]
        if node.right:
            node = node.right
            while node:
                stack.append(node)
                node = node.left
        else:
            node = stack.pop()
            while stack and stack[-1].right == node:
                node = stack.pop()


    def get_stack(self, node, target):
        stack = []
        while node:
            stack.append(node)
            if target <= node.val:
                node = node.left
            else:
                node = node.right
        return stack

