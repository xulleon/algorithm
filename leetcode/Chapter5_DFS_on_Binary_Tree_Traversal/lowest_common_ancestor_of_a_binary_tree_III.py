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

# Solution 2
# Runtime: 84 ms, faster than 5.99% of Python3 online submissions for Lowest Common Ancestor of a Binary Tree III.
# Memory Usage: 20 MB, less than 52.89% of Python3 online submissions for Lowest Common Ancestor of a Binary
class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if p is None or q is None:
            return None
        
        ps, qs = [], []
        
        while p:
            ps.insert(0, p)
            p = p.parent
            
        while q:
            qs.insert(0, q)
            q = q.parent

        cnts = min(len(ps), len(qs))
        for i in range(cnts):
            if ps[i] != qs[i]:
                return ps[i-1]
        return ps[i]
