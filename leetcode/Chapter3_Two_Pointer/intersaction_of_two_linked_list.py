# https://leetcode.com/problems/intersection-of-two-linked-lists/
# SOLUTION 1
# Runtime: 80 ms, faster than 62.50% of Python3 online submissions for Intersection of Two Linked Lists.
#Memory Usage: 27.2 MB, less than 68.48% of Python3 online submissions for Intersection of Two Linked Lists.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None
        
        nodeA, nodeB = headA, headB
        
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
            
        return nodeA

# SOLUTION 2
# Runtime: 88 ms, faster than 19.72% of Python3 online submissions for Intersection of Two Linked Lists.
# Memory Usage: 27.6 MB, less than 13.97% of Python3 online submissions for Intersection of Two Linked Lists.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# SOLUTION 1
from collections import defaultdict
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA is None or headB is None:
            return None

        visited = defaultdict(bool)
        node = headA
        while node:
            visited[node] = True
            node = node.next
            
        node = headB
        while node:
            if visited[node]:
                return node
            visited[node] = True
            node = node.next
            
        return None
  
