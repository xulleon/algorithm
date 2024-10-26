# https://leetcode.com/problems/linked-list-cycle/
# Runtime: 46 ms, faster than 49.96% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 19.2 MB, less than 30.77% of Python3 online submissions for Linked List Cycle.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return None
        
        slow, fast = head, head.next
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
            
        return False
