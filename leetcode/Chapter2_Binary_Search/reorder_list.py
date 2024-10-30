# https://leetcode.com/problems/reorder-list/
# Runtime: 4 ms, faster than 37.74% of Python3 online submissions for Reorder List.
# Memory Usage: 23.4 MB, less than 81.21% of Python3 online submissions for Reorder List.
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        pl, pr = head, head
        
        # add prev and find the last node
        while pr.next:
            tmp = pr
            pr = pr.next
            pr.prev = tmp
            
        while pl.next:
            if pl.next == pr:
                break
            last = pr
            pr = pr.prev
            pr.next = None
            next = pl.next
            pl.next = last
            last.next = next
            last.pre = None
            pl = next
            
        return head
            
