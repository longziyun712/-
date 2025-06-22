class TreeNode:
    def __init__(self, val): #通用
        self.val = val
        self.children=[]
def build(s):
    stack=[] #存放父节点
    node=None #记录前一个有子节点的节点
    for i in s:
        if i.isalpha():
            node=TreeNode(i)
            if stack:
                stack[-1].children.append(node) #stack顶是父节点，把子节点加进去
            else:
                root=node
        if i =='(': #说明后面是子节点
            stack.append(node)
        if i==')':
            stack.pop() #把父节点删掉
    return root

def preorder(node):
    if not node:
        return ''
    res=''
    res += node.val
    for child in node.children:
        res+=preorder(child)
    return res
def postorder(node):
    if not node:
        return ''
    res=''
    for child in node.children:
        res+=postorder(child)
    res += node.val
    return res
s=input().strip()
root=build(s)
print(preorder(root))
print(postorder(root))