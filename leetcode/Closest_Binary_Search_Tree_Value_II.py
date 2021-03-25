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
