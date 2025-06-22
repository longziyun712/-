# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res=[]
        def pre(node):
            if not node or len(res)==k:
                return
            pre(node.left)
            if len(res)==k:
                return
            res.append(node.val)
            pre(node.right)
        pre(root)
        return res[-1]
## BST的定义是左子树所有元素 < 此节点 < 右子树所有元素
