# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return -1
        q = [(root, 0)]
        s = []
        while q:
            r, i = q.pop(0)
            if r:
                if len(s) < i+1:
                    s.append(r.val)
                else:
                    s[i]+=r.val  
                q.append((r.left, i+1))
                q.append((r.right, i+1))
        s.sort()
        
        return s[-k] if k<=len(s) else -1