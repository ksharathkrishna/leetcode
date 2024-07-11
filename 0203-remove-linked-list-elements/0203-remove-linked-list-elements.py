# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            if curr.val == val:
                if prev and prev.next:
                    prev.next = prev.next.next
                    curr = curr.next
                else:
                    head = curr.next
                    curr = head
            else:
                prev = curr
                curr = curr.next
        return head
        