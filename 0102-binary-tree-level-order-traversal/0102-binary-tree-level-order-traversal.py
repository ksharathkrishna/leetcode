# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [(root, 0)]
        l = [[]]
        while q:
            r, i = q.pop(0)
            if len(l) < i+1:
                l.append([r.val])
            else:
                l[i].append(r.val)   
            if r.left:
                q.append((r.left, i+1))
            if r.right:
                q.append((r.right, i+1))
        return l