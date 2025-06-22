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
        result=[]
        queue=deque()
        queue.append(root)
        while queue:
            level=[]
            for _ in range(len(queue)):
                m=queue.popleft()
                level.append(m.val)
                if m.left:
                    queue.append(m.left)
                if m.right:
                    queue.append(m.right)
            result.append(level)
        return result
