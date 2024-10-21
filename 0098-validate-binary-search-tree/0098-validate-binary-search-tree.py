# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.prev_val = None
        return self.inord(root)
    
    def inord(self, root):
        if not root:
            return True
        
        lt = self.inord(root.left)

        if self.prev_val is not None and self.prev_val >= root.val:
                return False
        else:
            self.prev_val = root.val

        rt = self.inord(root.right)
        
        
        return lt and rt