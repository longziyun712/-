from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def build(index):
    if index>=len(lst):
        return None
    node=TreeNode(lst[index])
    node.left=build(2*index+1)
    node.right=build(2*index+2)
    return node
n=int(input())
lst=list(map(int,input().split()))
def dfs(node, path):
    path.append(node.val)
    if node.left is None and node.right is None:
        res.append(path.copy())
    if node.right is not None:
        dfs(node.right,path)
    if node.left is not None:
        dfs(node.left,path)
    path.pop() #子节点全部遍历完，回溯 换下一个节点
res=[]
dfs(build(0),[])
minmin=True
maxmax=True

for pa in res:
    print(*pa)
    for i in range(len(pa)-1):
        if pa[i]<pa[i+1]:
            maxmax=False
        if pa[i]>pa[i+1]:
            minmin=False
if minmin==True:
    print('Min Heap')
elif maxmax==True:
    print('Max Heap')
else:
    print('Not Heap')

