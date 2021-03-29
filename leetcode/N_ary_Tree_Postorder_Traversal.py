# https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        '''
        please node
        '''
        if root is None:
            return []
        res = []
        queue = [root]
        while queue:
            head = queue.pop()
            # This pop() instead of pop(0) like BFS,
            # it makes the whole sequence node -> right -> left
            # because it is always the last node which is the
            # right most to be added, leave the left most to be
            # delt with last. when reverse the whole process by
            # res[::-1], the whole process becomes
            # left -> right -> node, which is the postorder.
            if head is not None:
                res.append(head.val)
                for child in head.children:
                    queue.append(child)

        return res[::-1]
