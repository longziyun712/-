# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dui(p,q):
            if not p and not q: #都为空
                return True
            if not p or not q: #已抛出都为空的情况
                return False
            return (p.val==q.val and dui(p.left,q.right) and dui(p.right,q.left))
        return dui(root.left,root.right)
