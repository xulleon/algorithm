# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur = next = head
        pre = None
        while cur is not None:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        return pre
