# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""
# Recursive
# Runtime: 2541 ms, faster than 5.13% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree II.
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':

        def inorder(node):
            if node:
                yield from inorder(node.left)
                yield node
                yield from inorder(node.right)

        def hassubtree(node1, subnode):
            for node in inorder(node1):
                if node.val == subnode.val:
                    return True
            return False
        # Check if q is under p
        phasq = hassubtree(p, q)
        if phasq:
            return p
        # check if p is under q
        qhasp = hassubtree(q, p)
        if qhasp:
            return q

        # Then p and q must has a common parent
        # list all the parents of p
        pparents = []
        while p.parent:
            pparents.append(p.parent.val)
            p = p.parent

        # find which parent is the common one for p and q
        while q and q.parent:
            if q.parent.val in pparents:
                return q.parent
            q = q.parent

        return None
