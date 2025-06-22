class Treenode:
    def __init__(self,left=None,right=None):
        self.left=left
        self.right=right
def tree_height(node):
    if node is None:
        return -1
    return max(tree_height(node.left),tree_height(node.right))+1
def count_leaves(root):
    if root is None:
        return 0
    elif root.left is None and root.right is None:
        return 1
    return count_leaves(root.left)+count_leaves(root.right)
n=int(input())
nodes=[Treenode() for _ in range(n)]
is_son=[False]*n
for i in range(n):
    left,right=map(int,input().split())
    if left!=-1:
        nodes[i].left=nodes[left]
        is_son[left]=True
    if right!=-1:
        nodes[i].right=nodes[right]
        is_son[right]=True
root_index=is_son.index(False) #找到根节点
root=nodes[root_index]
print(tree_height(root),count_leaves(root))

