# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        if not(p or q):
            return True
        if not(p and q):
            return False

        l = self.isSameTree(p.left, q.left)
        if p.val != q.val:
            return False
        r =self.isSameTree(p.right,q.right)
        
        return l and r