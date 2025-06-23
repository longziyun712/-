# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        lst=[]
        lst+=self.inorderTraversal(root.left)  # 递归遍历左子树
        lst+=[root.val] # 访问根节点
        lst+=self.inorderTraversal(root.right)  # 递归遍历右子树
        return lst
