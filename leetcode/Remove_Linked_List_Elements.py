# https://leetcode.com/problems/remove-linked-list-elements/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        if head is None:
            return None

        prev = cur = head
        next = head.next
        while cur:
            if cur.val == val:
                # found the node and remove cur node
                cur.next = None
                if cur is head:
                    # first node is the target node
                    # try to remove the first one
                    head = next
                    prev = next
                else:
                    prev.next = next
            else:
                prev = cur
            cur = next
            if next is None:
                # reach the end of the link
                return head
            next = next.next
