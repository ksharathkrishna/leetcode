# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # check if kth node available
        c = 0
        curr = head
        while c<k:
            if not curr:
                return head
            c += 1
            curr = curr.next
        
        # reverse the remaing LL recursivly
        prev = self.reverseKGroup(curr, k)

        # reverse the current batch
        c = 0
        curr = head
        while c<k:
            # reverse LL logic
            nxt = curr.next
            curr.next = prev

            prev = curr
            curr = nxt
            c += 1

        return prev
        