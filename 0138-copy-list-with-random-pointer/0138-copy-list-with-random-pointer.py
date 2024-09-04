"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dup, dup1, dup2 = None, None, None
        head1, head2 = head, head
        map = {}
           
        while head1:
            new_n = Node(head1.val)
            if dup:
                dup.next = new_n
            else:
                dup1 = new_n
            dup = new_n
            head1 = head1.next

        res, dup2 = dup1, dup1
        while head2:
            map[head2] = dup1
            head2 = head2.next
            dup1 = dup1.next
        
        while head:
            dup2.random = map.get(head.random)
            dup2 = dup2.next
            head = head.next
        
        return res
            