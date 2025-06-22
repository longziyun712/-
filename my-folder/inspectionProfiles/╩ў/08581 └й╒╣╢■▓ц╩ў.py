class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
def build(s,index):
    if s[index]=='.':
        return None,index+1
    node=TreeNode(s[index])
    index+=1
    node.left,index=build(s,index)
    node.right,index=build(s,index)
    return node,index
def inorder(node):
    res=''
    if not node:
        return ''
    res+=str(inorder(node.left))
    res+=str(node.val)
    res+=str(inorder(node.right))
    return res
def postorder(node):
    res=''
    if not node:
        return ''
    res+=str(postorder(node.left))
    res+=str(postorder(node.right))
    res+=str(node.val)
    return res
s=input().strip()
root,_=build(s,0)
print(inorder(root))
print(postorder(root))