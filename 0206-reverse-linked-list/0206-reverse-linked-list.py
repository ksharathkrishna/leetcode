# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp, prev = None, None
        curr = head
        nxt = None
        
        while curr:
            temp = prev
            prev = curr
            nxt = curr.next
            curr.next = temp
            curr = nxt
        
        return prev