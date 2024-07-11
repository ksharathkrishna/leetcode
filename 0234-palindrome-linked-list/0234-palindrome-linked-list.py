# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        f = head
        stk = []
        while f:
            stk.append(f.val)
            f = f.next
        while head:
            if head.val != stk.pop():
                return False
            head = head.next
        return True