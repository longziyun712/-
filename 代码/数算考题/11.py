from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def build(index, lst):  # 添加 lst 参数
    if index >= len(lst):  # 修正终止条件
        return None
    node = TreeNode(lst[index])
    node.left = build(2 * index + 1, lst)  # 传递列表
    node.right = build(2 * index + 2, lst)
    return node

n = int(input())
lst = list(map(int, input().split()))

def dfs(node, path, res):  # 添加 res 参数
    if node is None:
        return
    path.append(node.val)  # 先记录当前节点值
    if node.left is None and node.right is None:
        res.append(path.copy())  # 正确保存路径
    dfs(node.left, path, res)    # 传递所有参数
    dfs(node.right, path, res)
    path.pop()  # 回溯

res = []
root = build(0, lst)  # 从索引0开始构建
dfs(root, [], res)
print(res)