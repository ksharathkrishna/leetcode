# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not root:
            return False
        
        # both trees are same
        if self.in_ord(root, subRoot):
            return True
    
        # Check if left or right sub tree is same recursively
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
    
    
    def in_ord(self, root, subRoot):

        if root is None and subRoot is None:
            return True
        if root is None or subRoot is None:
            return False
        lt = self.in_ord(root.left, subRoot.left)
        if root.val != subRoot.val:
            return False
        rt = self.in_ord(root.right, subRoot.right)
        return lt and rt