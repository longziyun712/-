### 一、输入输出和计概

牛的选举

```python
from collections import defaultdict #为缺失键自动创建
n,k=map(int,input().split())
dic=defaultdict()
for i in range(1,n+1):
    dic[i]=list(map(int,input().split()))
d=dict(sorted(dic.items(),key=lambda x:x[1][0],reverse=True)[:k]) #sorted是列表
n=sorted(d.items(),key=lambda x:x[1][1],reverse=True)[0][0]
print(n)
```

倒排索引查询

```python
from collections import defaultdict
N=int(input())
dct=defaultdict(list)
s=set()  ## 创建集合唯一方式
for i in range(N):  # 把词汇诸如ABC编成了0 1 2 …… N-1
    doc=list(map(int,input().split()))  #一定要全部转成整数！！！
    dct[i]=doc[1:]
    for j in doc[1:]:
        s.add(j)
M=int(input())
for i in range(M):
    lst=list(map(int,input().split()))  ##这里是字符串！！！！ 要转成数字 才能比 1 -1 0
    s1 = s.copy()
    #唯一初始化方法 通过每次在集合里增加和删减，减少遍历集合的时间复杂度。核心*****
    for x in range(N):
        if lst[x]==1:
            s1&=set(dct[x])  # 集合的交集符号 必须先交后减
        elif lst[x]==-1:
            s1-= set(dct[x]) # 左边集合去掉右边集合的元素
    if s1==set():
        print('NOT FOUND')
    else:
        print(*sorted(s1))
```

### 二、栈

##### 括号匹配

```python
ans = []
for s in lines:
    stack = []
    Mark = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
            Mark += ' '
        elif s[i] == ')':
            if len(stack) == 0:
                Mark += '?'
            else:
                Mark += ' '
                stack.pop()
        else:
            Mark += ' '
    while(len(stack)):
        Mark[stack[-1]] = '$'
        stack.pop()
    print(s)
    print(''.join(map(str, Mark)))
```

今日化学论文

```python
s=input()
stack=[]
for x in s:
    stack.append(x)
    if x ==']':
        stack.pop()
        helpstack=[]
        while stack[-1]!='[':
            helpstack.append(stack.pop())
        stack.pop()
        result = ''
        while helpstack[-1] in '0123456789':
            result+=helpstack.pop()
        helpstack=helpstack*int(result) #保证helpstack还是列表/栈
        while helpstack!=[]:
            stack.append(helpstack.pop())
print(*stack,sep='')
```

##### 中序转后序

基本步骤：

1. 初始化运算符栈和输出栈为空。
2. 从左到右遍历中缀表达式的每个符号。
   - 如果是操作数（数字），则将其添加到输出栈。
   - 如果是左括号，则将其推入运算符栈。
   - 如果是运算符：
     - 如果运算符的优先级大于运算符栈顶的运算符，或者运算符栈顶是左括号，则将当前运算符推入运算符栈。
     - 否则，将运算符栈顶的运算符弹出并添加到输出栈中，直到满足上述条件（或者运算符栈为空）。
     - 将当前运算符推入运算符栈。
   - 如果是右括号，则将运算符栈顶的运算符弹出并添加到输出栈中，直到遇到左括号。将左括号弹出但不添加到输出栈中。
3. 如果还有剩余的运算符在运算符栈中，将它们依次弹出并添加到输出栈中。
4. 输出栈中的元素就是转换后的后缀表达式。

```python
def infix_to_postfix(expression):
    precedence = {'+':1, '-':1, '*':2, '/':2}
    stack = []
    postfix = []
    number = ''

    for char in expression:
        if char.isnumeric() or char == '.':
            number += char
        else:
            if number:
                num = float(number)
                postfix.append(int(num) if num.is_integer() else num)
                number = ''
            if char in '+-*/':
                while stack and stack[-1] in '+-*/' and precedence[char] <= precedence[stack[-1]]:
                    postfix.append(stack.pop())
                stack.append(char)
            elif char == '(':
                stack.append(char)
            elif char == ')':
                while stack and stack[-1] != '(':
                    postfix.append(stack.pop())
                stack.pop()

    if number:
        num = float(number)
        postfix.append(int(num) if num.is_integer() else num)

    while stack:
        postfix.append(stack.pop())

    return ' '.join(str(x) for x in postfix)

n = int(input())
for _ in range(n):
    expression = input()
    print(infix_to_postfix(expression))
```

##### 后序求值

```python
n=int(input())
for _ in range(n):
    lst=input().split()
    stack=[]
    for s in lst:
        if s.isnumeric() or '.'in s :
            stack.append(float(s))
        else:
            b=stack.pop()
            a=stack.pop()
            if s=='+':
                stack.append(a+b)
            if s=='-':
                stack.append(a-b)
            if s=='*':
                stack.append(a*b)
            if s=='/':
                stack.append(a/b)
    print('%.2f'% float(stack[0]))
```

##### 十进制转换

```python
a=int(input())
if a==0:
    print(a)
else:
    stack=[]
    while a>0:
        stack.append(a%8)
        a=a//8
    result=''
    while stack:
        result+=str(stack.pop())
    print(result)
```

### 三、队列

##### 约瑟夫问题

```python
while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    lst=[i for i in range(1,a+1)]
    while len(lst)!=1:
        for j in range(b-1):
            lst.append(lst.pop(0))
        lst.pop(0)
    print(int(lst[0]))
```

##### 队列和栈

```python
m=int(input())
for _ in range(m):
    n=int(input())
    stack=[]
    queue=[]
    s = 1
    for __ in range(n):
        lst=input().split()
        if lst[0]=='push':
            stack.append(lst[1])
            queue.append(lst[1])
        else:
            if stack and queue:
                stack.pop()
                queue.pop(0)
            else:
                s=0
#  这里最开始是break然后直接命名queue和stack了 但是后续数据没有完整接收
#  导致最后应该有数据没有被读入！！！！牛牛牛
    if s==0:
        print('error','error',sep='\n')
    else:
        print(' '.join(queue))
        print(' '.join(stack))
```

##### 双端队列

```python
n=int(input())
for _ in range(n):
    m = int(input())
    lst = []
    for __ in range(m):
        a,b=map(int,input().split())
        if a==1:
            lst.append(b)
        else:
            if b==0:
                lst.pop(0)
            else:
                lst.pop()
    if lst:
        print(*lst)
    else:
        print('NULL')
```

### 四、树（注意根是不是空）

长子-兄弟法

```python
class Node: 
	def __init__(self, data): 
		self.data = data 
		self.firstChild = None
		self.nextSibling = None
```

##### 树的高度

```python
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left_height=self.maxDepth(root.left)
        right_height=self.maxDepth(root.right)
        return max(left_height,right_height)+1
```

##### 需要找根的建树  求二叉树高度和子叶数目

```python
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
root_index=is_son.index(False)   #找到根节点
root=nodes[root_index]
print(tree_height(root),count_leaves(root))
```

##### 两树是否相同

```python
def is_same_tree(p, q):
    if not p and not q:
        return True
    if not p or not q:
        return False
    return (p.val == q.val and is_same_tree(p.left, q.left) and 
            					is_same_tree(p.right, q.right))
```

##### 翻转二叉树

```python
def invert_tree(root):
    if root:
        root.left, root.right = invert_tree(root.right), invert_tree(root.left)
    return root
```

##### 二叉搜索树 BST 左子树<根<右子树

```python
def find_min(root):
    if not root.left:
        return root.val
    return find_min(root.left)
def find_max(root):
    if not root.right:
        return root.val
    return find_max(root.right)
```

##### 二叉搜索树第K小元素

```python
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
```

##### 遍历树

```python
from collections import defaultdict
import sys
sys.setrecursionlimit(10000)
def main():
    n = int(sys.stdin.readline())
    tree = defaultdict(list)
    all_nodes = set()
    child_nodes = set()   
    for _ in range(n):
        parts = list(map(int, sys.stdin.readline().split()))
        parent, *children = parts
        tree[parent].extend(children)
        all_nodes.add(parent)
        all_nodes.update(children)
        child_nodes.update(children)   
    # 根节点 = 出现在 all_nodes 但没出现在 child_nodes 的那个
    root = (all_nodes - child_nodes).pop()
    def traverse(u):
        # 把 u 自己和它的所有直接孩子放一起排序
        group = tree[u] + [u]
        group.sort()
        for x in group:
            if x == u:
                print(u)
            else:
                traverse(x)  
    traverse(root)
if __name__ == "__main__":
    main()
```

##### 前序和中序构造二叉树

```python
def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder or not inorder:
        return None
    root = TreeNode(preorder[0])
    n = inorder.index(preorder[0])
    root.left = self.buildTree(preorder[1:n + 1], inorder[:n])
    root.right = self.buildTree(preorder[n + 1:], inorder[n + 1:])
    return root
```

##### 二叉搜索树BST的层序遍历

```python
def build(lst):
    if not lst:
        return None
    root=TreeNode(lst[0])
    root.left=build(list(x for x in lst[1:] if x<lst[0])) #生成式需要转列表
    root.right=build(list(x for x in lst[1:] if x>lst[0]))
    return root
```

##### 平衡二叉树节点![image-20250602214708342](C:\Users\msm\AppData\Roaming\Typora\typora-user-images\image-20250602214708342.png)

是否平衡树AVL 每个节点的左右子树高度差不超过1

```python
def is_balanced(root):
    def check_height(node):
        if not node:
            return 0
        left_height = check_height(node.left)
        if left_height == -1:
            return -1  # Left subtree is unbalanced
        right_height = check_height(node.right)
        if right_height == -1:
            return -1  # Right subtree is unbalanced
        if abs(left_height - right_height) > 1:
            return -1  # Current node is unbalanced
        return max(left_height, right_height) + 1
    return check_height(root) != -1
```

### 五、堆

优先级：最大最小堆 heapq默认向下调整 形成最小堆

向上调整：和父节点比较 建堆：从索引 1 开始

向下调整：和子节点比较 建堆：从 (n-2)//2 开始

##### 向下调整大顶堆

```python
import heapq
n=int(input())
lst=list(map(int,input().split()))
reverse=[]
for i in lst:
    reverse.append(-i)
heapq.heapify(reverse)
res=[]
for i in list(reverse):
    res.append(-i)
print(*res)
```

##### 向上调整大顶堆

```python
n=int(input())
lst=list(map(int,input().split()))

for i in range(n):
    while i>=0:
        if (i-1)//2>=0 and lst[(i-1)//2]<lst[i]:
            lst[(i-1)//2],lst[i]=lst[i],lst[(i-1)//2]
            i=(i-1)//2
        else:
            break
print(*lst)
```

##### 霍夫曼树

```python
import heapq
n=int(input())
lst=list(map(int,input().split()))
heapq.heapify(lst)
res=0
while len(lst)>1:
    a=heapq.heappop(lst)
    b=heapq.heappop(lst)
    he=a+b
    res+=he
    heapq.heappush(lst,he)
print(res)
```

##### 堆路径

```python
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
```

### 六、图

##### 所有路径

```python
def allPathsSourceTarget(self, graph):
    def dfs(node, path, visited):
        if node == len(graph) - 1:  # 到达终点
            res.append(path.copy())  # 注意要用copy()
            return
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)          # 标记已访问
                path.append(neighbor)          # 加入路径
                dfs(neighbor, path, visited)   # 递归
                path.pop()                     # 回溯
                visited.remove(neighbor)       # 撤销标记
        res = []
        dfs(0, [0], set([0])) 
        return res
```

##### 无向图 连通块

```python
n, m = map(int, input().split())
adjlist = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adjlist[u].append(v)
    adjlist[v].append(u)
def dfs(node,visited):
    visited[node]=True
    for next in adjlist[node]:
        if not visited[next]:
            dfs(next,visited)
visited=[False]*(n)
num=0
for i in range(n):
    if not visited[i]:
        dfs(i,visited)
        num+=1
print(num)
```

##### 有向图 判环

```python
n, m = map(int, input().split())
adjlist = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adjlist[u].append(v)
def dfs(node,visited):
    if track[node]==True:
        return True
    if visited[node]==True:
        return False
    else:
        visited[node] = True
        track[node]=True
    for next in adjlist[node]:
         if dfs(next,visited):
             return True
    track[node] = False #循环完就回溯
    return False
visited = [False] * (n)
track= [False] * (n)
res='No'
for i in range(n):
    if dfs(i,visited):
        res='Yes'
print(res)
```

##### 拓扑排序 Topological Sorting

**有向无环图（DAG）,** 每一条有向边 `(u, v)`，`u` 在排序中总是位于 `v` 的前面

```python
from collections import deque, defaultdict
def topological_sort(graph):
    indegree = defaultdict(int)
    result = []
    queue = deque()
    # 计算每个顶点的入度
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1
    # 将入度为 0 的顶点加入队列
    for u in graph:
        if indegree[u] == 0:
            queue.append(u)
    # 执行拓扑排序
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    # 检查是否存在环
    if len(result) == len(graph):
        return result
    else:
        return None
```

##### 最小生成树 Minimum Spanning Tree 

##### Kruskal

```python
class DisjointSet:
    def __init__(self, num_vertices):
        self.parent = list(range(num_vertices))
        self.rank = [0] * num_vertices
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            elif self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            else:
                self.parent[root_x] = root_y
                self.rank[root_y] += 1
def kruskal(graph):
    num_vertices = len(graph)
    edges = []
    # 构建边集
    for i in range(num_vertices):
        for j in range(i + 1, num_vertices):
            if graph[i][j] != 0:
                edges.append((i, j, graph[i][j]))
    # 按照权重排序
    edges.sort(key=lambda x: x[2])
    # 初始化并查集
    disjoint_set = DisjointSet(num_vertices)
    # 构建最小生成树的边集
    minimum_spanning_tree = []
    for edge in edges:
        u, v, weight = edge
        if disjoint_set.find(u) != disjoint_set.find(v):
            disjoint_set.union(u, v)
            minimum_spanning_tree.append((u, v, weight))
    return minimum_spanning_tree
```

##### Prim

```python
import heapq
def prim(graph, start):
    """ :param graph: 邻接表表示的图，格式 {u: [(v, weight), ...]}
    :param start: 起始顶点
    :return: MST 的边列表 [(u, v, weight), ...]"""
    V = len(graph)
    visited = [False] * V  # 记录顶点是否已加入 MST
    heap = []  # 优先队列（最小堆）
    mst_edges = []  # 存储 MST 的边
    # 初始化：将起始点的所有边加入堆
    visited[start] = True
    for v, weight in graph[start]:
        heapq.heappush(heap, (weight, start, v))
    while heap and len(mst_edges) < V - 1:
        weight, u, v = heapq.heappop(heap)
        if visited[v]:
            continue  # 跳过已访问的顶点
        visited[v] = True
        mst_edges.append((u, v, weight))
        # 将新加入顶点的边加入堆
        for neighbor, w in graph[v]:
            if not visited[neighbor]:
                heapq.heappush(heap, (w, v, neighbor))
    return mst_edges
```

##### 最短路径

#### Dijkstra

```python
import heapq
def dijkstra(graph, start):
    # 初始化距离数组
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    # 优先队列：(距离, 节点)
    heap = [(0, start)]
    while heap:
        current_dist, node = heapq.heappop(heap)
        # 如果当前距离大于已知最短距离，跳过
        if current_dist > dist[node]:
            continue
        # 遍历所有邻居
        for neighbor, weight in graph[node]:
            new_dist = current_dist + weight
            # 如果找到更短路径
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(heap, (new_dist, neighbor))
    return dist
-------------------------------#记录路径  添加prev数组记录前驱节点
def dijkstra_with_path(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    prev = [-1] * n  # 记录前驱节点
    dist[start] = 0
    heap = [(0, start)]
    while heap:
        d, u = heapq.heappop(heap)
        if d != dist[u]:
            continue
        for v, w in graph[u]:
            new_dist = d + w
            if new_dist < dist[v]:
                dist[v] = new_dist
                prev[v] = u  # 记录前驱节点
                heapq.heappush(heap, (new_dist, v))
    return dist, prev
# 重建路径
def get_path(prev, target):
    path = []
    while target != -1:
        path.append(target)
        target = prev[target]
    return path[::-1]  # 反转得到正向路径
```

#### Floyd-Warshall

```python
def floyd_warshall(graph):
    n = len(graph)
    dist = [[float('inf')] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j:
                dist[i][j] = 0
            elif j in graph[i]:
                dist[i][j] = graph[i][j]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    return dist
```

最大权值连通块

```python
from collections import deque
n, m = map(int, input().split())
lst=list(map(int, input().split()))
adjlist = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adjlist[u].append(v)
    adjlist[v].append(u)
visited = [False] * n
def bfs(node,res):
    queue=deque()
    queue.append(node)
    res+=lst[node]
    visited[node]=True
    while queue:
        a=queue.popleft()
        for i in adjlist[a]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
                res +=lst[i]
    return res
result=[]
for _ in range(n):
    if not visited[_]:
        result.append(bfs(_,0))
print(max(result))
```

迷宫最短路径 

```python
from collections import deque
MAX_DIRECTIONS = 4
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def is_valid_move(x, y):
    return 0 <= x < n and 0 <= y < m and maze[x][y] == 0 and not in_queue[x][y]
def bfs(start_x, start_y):
    queue = deque()
    queue.append((start_x, start_y))
    in_queue[start_x][start_y] = True
    while queue:
        x, y = queue.popleft()
        if x == n - 1 and y == m - 1:
            return
        for i in range(MAX_DIRECTIONS):
            next_x = x + dx[i]
            next_y = y + dy[i]
            if is_valid_move(next_x, next_y):
                prev[next_x][next_y] = (x, y)
                in_queue[next_x][next_y] = True
                queue.append((next_x, next_y))
def print_path(pos):
    prev_position = prev[pos[0]][pos[1]]
    if prev_position == (-1, -1):
        print(pos[0] + 1, pos[1] + 1)
        return
    print_path(prev_position)
    print(pos[0] + 1, pos[1] + 1)
n, m = map(int, input().split())
maze = [list(map(int, input().split())) for _ in range(n)]
in_queue = [[False] * m for _ in range(n)]
prev = [[(-1, -1)] * m for _ in range(n)]
bfs(0, 0)
print_path((n - 1, m - 1))

```

词梯

```python
from collections import defaultdict
dic=defaultdict(list)
n,lis=int(input()),[]
for i in range(n):
    lis.append(input())
for word in lis:
    for i in range(len(word)):
        bucket=word[:i]+'_'+word[i+1:]
        dic[bucket].append(word)
def bfs(start,end,dic):
    queue=[(start,[start])]
    visited=[start]
    while queue:
        currentword,currentpath=queue.pop(0)
        if currentword==end:
            return ' '.join(currentpath)
        for i in range(len(currentword)):
            bucket=currentword[:i]+'_'+currentword[i+1:]
            for nbr in dic[bucket]:
                if nbr not in visited:
                    visited.append(nbr)
                    newpath=currentpath+[nbr]
                    queue.append((nbr,newpath))
    return 'NO'
start,end=map(str,input().split())    
print(bfs(start,end,dic))
```

骑士周游

```python
def knight_tour():
    import sys
    sys.setrecursionlimit(1000000)  # 防止递归深度过大报错
    n = int(sys.stdin.readline())  # 棋盘大小
    sr, sc = map(int, sys.stdin.readline().split())  # 起始位置
    board = [[-1 for _ in range(n)] for _ in range(n)]  # 初始化棋盘（-1表示未访问）
    # 骑士的8种移动方向（“日”字形）
    moves = [ (2, 1), (1, 2), (-1, 2), (-2, 1),
        (-2, -1), (-1, -2), (1, -2), (2, -1)]
    def is_valid(x, y):
        """检查位置(x,y)是否在棋盘内且未访问"""
        return 0 <= x < n and 0 <= y < n and board[x][y] == -1
    def get_next_moves(x, y):
        """动态排序下一步：优先选择后续分支少的位置（Warnsdorff规则）"""
        candidates = []
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            if is_valid(nx, ny):
                # 计算(nx,ny)的下一步可行数
                count = 0
                for ddx, ddy in moves:
                    nnx, nny = nx + ddx, ny + ddy
                    if is_valid(nnx, nny):
                        count += 1
                candidates.append((count, nx, ny))
        # 按可行数升序排序，优先尝试分支少的位置
        candidates.sort()
        return [(nx, ny) for _, nx, ny in candidates]
    def dfs(x, y, step):
        """DFS搜索路径"""
        if step == n * n:  # 终止条件：所有格子已访问
            return True
        for nx, ny in get_next_moves(x, y):  # 按优化顺序尝试下一步
            board[nx][ny] = step  # 标记访问
            if dfs(nx, ny, step + 1):  # 递归
                return True
            board[nx][ny] = -1  # 回溯
        return False
    # 从起始位置开始搜索
    board[sr][sc] = 0
    if dfs(sr, sc, 1):
        print("success")
    else:
        print("fail")
knight_tour()
```

马走日

```python
maxn = 10;
sx = [-2,-1,1,2, 2, 1,-1,-2]
sy = [ 1, 2,2,1,-1,-2,-2,-1]
ans = 0;
def Dfs(dep: int, x: int, y: int):
    #是否已经全部走完
    if n*m == dep:
        global ans
        ans += 1
        return
    #对于每个可以走的点
    for r in range(8):
        s = x + sx[r]
        t = y + sy[r]
        if chess[s][t]==False and 0<=s<n and 0<=t<m :
            chess[s][t]=True
            Dfs(dep+1, s, t)
            chess[s][t] = False; #回溯
for _ in range(int(input())):
    n,m,x,y = map(int, input().split())
    chess = [[False]*maxn for _ in range(maxn)]  #False表示没有走过
    ans = 0
    chess[x][y] = True
    Dfs(1, x, y)
    print(ans)
```

八皇后

```python
answer = []
def Queen(s):
    for col in range(1, 9):
        for j in range(len(s)):
            if (str(col) == s[j] or # 两个皇后不能在同一列
                    abs(col - int(s[j])) == abs(len(s) - j)): # 两个皇后不能在同一斜线
                break
        else:
            if len(s) == 7:
                answer.append(s + str(col))
            else:
                Queen(s + str(col))
Queen('')
n = int(input())
for _ in range(n):
    a = int(input())
    print(answer[a - 1])
```

##### 强连通单元 Kosaraju / 2 DFS

1. **第一次DFS**：在第一次DFS中，我们对图进行标准的深度优先搜索，但是在此过程中，我们记录下顶点完成搜索的顺序。这一步的目的是为了找出每个顶点的完成时间（即结束时间）。
2. **反向图**：接下来，我们对原图取反，即将所有的边方向反转，得到反向图。
3. **第二次DFS**：在第二次DFS中，我们按照第一步中记录的顶点完成时间的逆序，对反向图进行DFS。这样，我们将找出反向图中的强连通分量。

```python
def dfs1(graph, node, visited, stack):
    visited[node] = True
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs1(graph, neighbor, visited, stack)
    stack.append(node)
def dfs2(graph, node, visited, component):
    visited[node] = True
    component.append(node)
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dfs2(graph, neighbor, visited, component)
def kosaraju(graph):
    # Step 1: Perform first DFS to get finishing times
    stack = []
    visited = [False] * len(graph)
    for node in range(len(graph)):
        if not visited[node]:
            dfs1(graph, node, visited, stack)
    # Step 2: Transpose the graph
    transposed_graph = [[] for _ in range(len(graph))]
    for node in range(len(graph)):
        for neighbor in graph[node]:
            transposed_graph[neighbor].append(node)
    # Step 3: Perform second DFS on the transposed graph to find SCCs
    visited = [False] * len(graph)
    sccs = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            scc = []
            dfs2(transposed_graph, node, visited, scc)
            sccs.append(scc)
    return sccs
# Example
graph = [[1], [2, 4], [3, 5], [0, 6], [5], [4], [7], [5, 6]]
sccs = kosaraju(graph)
print("Strongly Connected Components:")
for scc in sccs:
    print(scc)
"""Strongly Connected Components:
[0, 3, 2, 1]
[6, 7]
[5, 4]"""
```

双指针

```python
n=int(input())
a=list(map(int,input().split()))
M = int(input())
i,j=0,n-1
while i<j:
    if a[i]+a[j]==M:
        print(a[i],a[j])
        i+=1
        j-=1
    elif a[i]+a[j]<M:
        i+=1
    elif a[i] + a[j] < M:
        j-=1
```

二分法

```python
left, right = 0, len(nums) - 1
while left <= right:
    mid = left + (right - left) // 2  # 避免溢出
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1
return -1  # 未找到
```

滑动窗口

```python
def sliding_window_fixed(nums, k):
    n = len(nums)
    if n < k:
        return None 
    window_sum = sum(nums[:k])
    max_sum = window_sum  
    for i in range(k, n):
        window_sum = window_sum + nums[i] - nums[i - k]
        max_sum = max(max_sum, window_sum)    
    return max_sum

def sliding_window_variable(s, target):
    from collections import defaultdict  
    left = 0
    window = defaultdict(int)
    result = 0    
    for right in range(len(s)):
        # 扩展右边界
        window[s[right]] += 1      
        # 收缩左边界（当窗口不满足条件时）
        while window[s[right]] > target:
            window[s[left]] -= 1
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
        # 更新结果
        result = max(result, right - left + 1)
    return result
```

单调栈

```python
def monotonic_increasing_stack(nums):
    stack = []
    for num in nums:
        # 维护栈的单调递增性（栈顶元素小于当前元素）
        while stack and stack[-1] > num:
            # 这里可以根据需要处理弹出的元素
            stack.pop()
        stack.append(num)
    return stack
```

最小栈

```python
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []  # 辅助栈，栈顶始终是当前最小值
    
    def push(self, x):
        self.stack.append(x)
        # 维护最小栈
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
    
    def pop(self):
        if self.stack.pop() == self.min_stack[-1]:
            self.min_stack.pop()
    
    def top(self):
        return self.stack[-1]
    
    def getMin(self):
        return self.min_stack[-1]
```

八皇后

```python
def solve_n_queens(n):
    solutions = []  # 存储所有解决方案的列表
    queens = [-1] * n  # 存储每一行皇后所在的列数
 
    def backtrack(row):
        if row == n:  # 找到一个合法解决方案
            solutions.append(queens.copy())
        else:
            for col in range(n):
                if is_valid(row, col):  # 检查当前位置是否合法
                    queens[row] = col  # 在当前行放置皇后
                    backtrack(row + 1)  # 递归处理下一行
                    queens[row] = -1  # 回溯，撤销当前行的选择
    
    def is_valid(row, col):
        for r in range(row):
            if queens[r] == col or abs(row - r) == abs(col - queens[r]):
                #前面棋子和这个col不在一列 也不能在同一个对角线上
                return False
        return True
        
    backtrack(0)  # 从第一行开始回溯
    return solutions
  # 获取第 b 个皇后串
def get_queen_string(b):
    solutions = solve_n_queens(8)
    if b > len(solutions):
        return None
    queen_string = ''.join(str(col + 1) for col in solutions[b - 1])
    return queen_string
    
test_cases = int(input())  # 输入的测试数据组数
for _ in range(test_cases):
    b = int(input())  # 输入的 b 值
    queen_string = get_queen_string(b)
    print(queen_string)
```

backstacking方法

```python
def solve_n_queens(n):
    stack = []  # 用于保存状态的栈
    solutions = []  # 存储所有解决方案的列表

    stack.append((0, [-1] * n))  # 初始状态为第一行，所有列都未放置皇后

    while stack:
        row, queens = stack.pop()

        if row == n:  # 找到一个合法解决方案
            solutions.append(queens.copy())
        else:
            for col in range(n):
                if is_valid(row, col, queens):  # 检查当前位置是否合法
                    new_queens = queens.copy()
                    new_queens[row] = col  # 在当前行放置皇后
                    stack.append((row + 1, new_queens))  # 推进到下一行

    return solutions
```

括号嵌套二叉树

```python
def parse_tree(s):  """ 解析括号嵌套格式的二叉树 """
    if s == '*':  # 处理空树
        return None
    if '(' not in s:  # 只有单个根节点
        return TreeNode(s)
    root_value = s[0]  # 根节点值
    subtrees = s[2:-1]  # 去掉根节点和外层括号
    # 使用栈找到逗号位置
    stack = []
    comma_index = None
    for i, char in enumerate(subtrees):
        if char == '(':
            stack.append(char)
        elif char == ')':
            stack.pop()
        elif char == ',' and not stack:
            comma_index = i
            break
    left_subtree = subtrees[:comma_index] if comma_index is not None else subtrees
    right_subtree = subtrees[comma_index + 1:] if comma_index is not None else None
    
    root = TreeNode(root_value)
    root.left = parse_tree(left_subtree)  # 解析左子树
    root.right = parse_tree(right_subtree) if right_subtree else None  # 解析右子树
    return root
```

扩展二叉树

```python
def build_tree(s, index):
    # 如果当前字符为'.'，表示空结点，返回None，并将索引后移一位
    if s[index] == '.':
        return None, index + 1
    # 否则创建一个结点
    node = Node(s[index])
    index += 1
    # 递归构造左子树
    node.left, index = build_tree(s, index)
    # 递归构造右子树
    node.right, index = build_tree(s, index)
    return node, index
```

括号嵌套树

```python
class TreeNode:
    def __init__(self, value): #类似字典
        self.value = value
        self.children = []
def parse_tree(s):
    stack = []
    node = None
    for char in s:
        if char.isalpha():  # 如果是字母，创建新节点
            node = TreeNode(char)
            if stack:  # 如果栈不为空，把节点作为子节点加入到栈顶节点的子节点列表中
                stack[-1].children.append(node)
        elif char == '(':  # 遇到左括号，当前节点可能会有子节点
            if node:
                stack.append(node)  # 把当前节点推入栈中
                node = None
        elif char == ')':  # 遇到右括号，子节点列表结束
            if stack:
                node = stack.pop()  # 弹出当前节点
    return node  # 根节点
```

# 链表

建链表 想要插队的Y君

```python
class Node:
	def __init__(self, data, next=None):
		self.data, self.next = data, next

class LinkList:
	def __init__(self):
		self.head = None
	def initList(self, data):
		self.head = Node(data[0])
		p = self.head
		for i in data[1:]:
			node = Node(i)
			p.next = node
			p = p.next
	def insertCat(self):
                if self.head==None:
                    self.head=Node(6)
                    return
                slow=fast=self.head
                while fast.next and fast.next.next:  #不能是next.next在前
                    slow=slow.next
                    fast=fast.next.next
                nd=Node(6)
                nd.next=slow.next
                slow.next=nd
	def printLk(self):
		p = self.head
		while p:
			print(p.data, end=" ")
			p = p.next
		print()

lst = list(map(int,input().split()))
lkList = LinkList()
lkList.initList(lst)
lkList.insertCat()
lkList.printLk()
```

快慢指针：查找链表中间节点

```python
slow,fast=head,head
while fast.next and fast.next.next:
    slow=slow.next
    fast=fast.next.next
mid = slow
```

反转链表：

单链表：

```python
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        current=head
        while current:
            a=current.next #保存下一个节点，因为下一行改结构这个点就没了
            current.next=prev
            prev=current # 把prev赋值到当前节点
            current=a #指针 索引到原链表的下一个节点
        return prev
```

双链表：

```python
def fan(head):
    pre,nt=None,None
    while head!=None:
        nt=head.next
        head.next=pre
        head.last=nt#last表示上一个
        pre=head
        head=nt
    return pre
```

回文链表

```python
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow

        prev = None
        current = mid
        while current:
            a = current.next
            current.next = prev
            prev = current
            current = a
        l, r = head, prev
        while l != mid:
            if l.val != r.val:
                return False
            l = l.next
            r = r.next
        return True
```

合并两个有序链表

```python
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode(-100,None)
        current=head
        while list1 and list2:
            if list1.val<=list2.val:
                current.next=list1 # 虚拟头节点
                list1=list1.next # 当前指针
            else:
                current.next=list2
                list2=list2.next
            current=current.next
        current.next=list1 if list1 is not None else list2
        return head.next
```

链表判断环：

```python
def detectCycle(head):
    if head is None or head.next is None or head.next.next is None:
        return None
    slow=head.next
    fast=head.next.next
    while slow!=fast:
        if fast.next is None or fast.next.next is None:
            return None
        slow=slow.next
        fast=fast.next.next
    fast=head
    while slow!=fast:
        slow=slow.next
        fast=fast.next
    return slow
```

### 散列表

```python
def insert_hash_table(keys, M):
    table = [0.5] * M  # 用 0.5 表示空位
    result = []
    for key in keys:
        index = key % M
        i = index
        while True:
            if table[i] == 0.5 or table[i] == key:
                result.append(i)
                table[i] = key
                break
            i = (i + 1) % M
    return result
# 使用标准输入读取数据
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])
keys = list(map(int, data[2:2 + N]))
positions = insert_hash_table(keys, M)
print(*positions)
```

KMP

```python
def build_next(pattern):
    next = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = next[j - 1]  #退回未匹配时候 重新计算next中的前后缀长度
        if pattern[i] == pattern[j]:
            j += 1
        next[i] = j
    return next
def kmp_search(text, pattern):
    next = build_next(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = next[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            print(f"Found at index {i - j + 1}")
            j = next[j - 1]
# 示例
text = "ABCABDABCABE"
pattern = "ABCABE"
kmp_search(text, pattern)  # 输出: Found at index 6
```

