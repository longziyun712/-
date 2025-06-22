from collections import deque
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.left=left
        self.right=right
def build(lst):
    if not lst:
        return None
    root=TreeNode(lst[0])
    root.left=build(list(x for x in lst[1:] if x<lst[0])) #生成式需要转列表
    root.right=build(list(x for x in lst[1:] if x>lst[0]))
    return root
def levelorder(root):
    if not root:
        return []
    queue=deque([root])
    res=[]
    while queue:
        node=queue.popleft()
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        res.append(node.val)
    return res

lst=list(map(int,input().split()))
lst1 = list(dict.fromkeys(lst)) #列表去重
print(*levelorder(build(lst1)))