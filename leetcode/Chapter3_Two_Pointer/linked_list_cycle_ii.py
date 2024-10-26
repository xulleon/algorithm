# https://leetcode.com/problems/linked-list-cycle-ii/
# Runtime: 50 ms, faster than 67.90% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 19 MB, less than 63.93% of Python3 online submissions for Linked List Cycle II.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        
        slow, fast = head, head
        
        cycle_node = None
        # Step 1: find the joint point
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
                
        # find the entry point
        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next

        return slow
