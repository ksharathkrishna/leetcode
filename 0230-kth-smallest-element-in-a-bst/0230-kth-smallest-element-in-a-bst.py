# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def inorder(root):
            if root is None: return None
            left = inorder(root.left)
            if left is not None: return left
            self.c += 1
            if self.c==k: return root.val
            return inorder(root.right)
        self.c = 0   
        ans = inorder(root)
        return ans