### 一、输入输出和计概

**File** ⼀>**Settings** ⼀>**Editor**⼀>**General**⾥ 的**Mouse Control**把**Change font size with Ctrl+Mouse Wheel**打上对勾，点击**OK**即可

```python
from collections import deque defaultdict
for i,x in enumerate(list),遍历list中的（下标，值）对
lst1 = list(dict.fromkeys(lst)) #列表去重
```

```python
import sys
data=sys.stdin.readline().strip() #读取一行
data = sys.stdin.read().strip().split() #一次性读入

while True:  #oj提交使用
    try:
        lines.append(input())
    except EOFError:
        break
# 输入方式2：空行终止 pc运行使用
while True:
    line = input().strip()
    if line == "":
        break
    lines.append(line)
```

```python
name = "Alice"
print(f"Hello {name}!")  # 输出：Hello Alice!
pi = 3.14159
print(f"π 保留两位小数: {pi:.2f}")  # 输出：π 保留两位小数: 3.14
for i in range(9):
    print(f'Queue{i+1}:'+' '.join(queues[i]))
    
#键值对输出
user = {"name": "Alice", "age": 30}
print(f"Name: {user['name']}, Age: {user['age']}")  # 输出：Name: Alice, Age: 30
#format 
text = "Name: {name}, Age: {age}".format(name="Bob", age=30)
print(text)  # 输出: Name: Bob, Age: 30

print(''.join(list))    print(*list)
print(''.join(map(str, Mark)))
```

```python
#RE (Runtime Error)： #类型错误、指针越界、除以0
# 递归爆栈
from sys import setrecurisonlimit
setrecursionlimit(10000) #python 默认 200
#TLE (Time Limit Exceeded)： 算法效率问题或死循环导致。
```

|   **操作**   | **列表 (`list`)**  | **双端队列 (`deque`)** |
| :----------: | :----------------: | :--------------------: |
| **左侧弹出** |    `lst.pop(0)`    |   `deque.popleft()`    |
| **右侧弹出** |    `lst.pop()`     |     `deque.pop()`      |
| **左侧插入** | `lst.insert(0, x)` | `deque.appendleft(x)`  |
| **右侧插入** |  `lst.append(x)`   |   `deque.append(x)`    |

### 四、树（注意根是不是空）

##### 建树 （后面有找根的情况）

```python
class Treenode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```

##### 给出每个节点的子节点，建树

```python
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
root_index=is_son.index(False)  #找到根节点
```

##### 完全二叉树建树

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
```

##### 前序：根-左-右        中序：左-根-右        后序：左-右-根 

```python
def preorder_traversal(root):
    if root:
        print(root.val)  # 访问根节点
        preorder_traversal(root.left)  # 递归遍历左子树
        preorder_traversal(root.right)  # 递归遍历右子树
```

##### 层序遍历

```python
#不分层
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
#分层
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
```

### 并查集（Disjoint Set）

```python
def find(a):
    if parent[a]!=a:
        parent[a]=find(parent[a])
    return parent[a]
def union(a,b):
    p=find(a)
    q=find(b)
    if p!=q:
        if size[p]>size[q]:
            parent[q]=p
            size[p]+=size[q]
        else:
            parent[p] = q
            size[q] += size[p]
n,m=map(int,input().split())
parent=list(range(n+1))  #这是从0到n，不然没有n了
size=[1]*(n+1)          # 多取一个
for _ in range(m):
    a,b=list(map(int,input().split()))
    union(a,b)
classes = [total[x] for x in range(1, n + 1) if x == parent[x]] #多少个集合 注意从1开始
```

##### 班级最高分

```python
def find(a):
    if parent[a]!=a:
        parent[a]=find(parent[a])
    return parent[a]
def union(a,b):
    p=find(a)
    q=find(b)
    if p!=q:
        parent[q] = p
        total[p]+=total[q]
        lst[p-1]=max(lst[p-1],lst[q-1])  #把班级根节点的成绩改成班级最大值去
n,m=map(int,input().split())
lst=list(map(int,input().split()))
parent=list(range(n+1))
total=[1]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    union(a,b)
root_count = 0
for i in range(1, n + 1):
    if parent[i] == i:
        root_count += 1
scores=[lst[find(a)-1] for a in range(1,n+1) if a==parent[a]] #提取根节点的成绩
print(root_count)
scores.sort(reverse=True)
print(*scores)
```

### heapq

```python
import heapq
heapq.heapify(lst)
heapq.heappop(lst)
heapq.heappush(lst,add)
```

### 六、图

##### 建图

```python
n,m=map(int,input().split())
lst=[[]for _ in range(n)]
for i in range(m):
    a,b=map(int,input().split())
    lst[a].append(b)
    lst[b].append(a)
```

##### BFS 宽搜

```python
from collections import deque
def bfs(node,res,n):
    visited[node]=0
    queue=deque()
    queue.append(node)
    traversal_order = [] 
    while queue:
        a=queue.popleft()
        traversal_order.append(a)
        for i in adjlist[a]:
            if visited[i]==-1:
                queue.append(i)
                visited[i]=visited[a]+1
    return visited
visited=[-1]*(n) #或者是False  然后改True
```

##### DFS 广搜

```python
def dfs(v, visited=None):
    if visited is None:
        visited = set()
        visited.add(v)
    print(v, end=' ')
    for neighbour in graph[v]:
        if neighbour not in visited:
            DFS(neighbour, visited)
```

————

##### 强连通单元是指有向图中的一个**极大子图**，其中任意两个顶点**互相可达**（即对于子图中的任意顶点u和v，存在从u到v的路径，也存在从v到u的路径）。

##### ————

##### Dijkstra算法（单源最短路径）贪心算法，每次从**未处理的顶点**中选择当前距离起点最近的顶点，并松弛其邻边。

##### 有权图Dijkstra, 无权图BFS

##### Floyd-Warshall算法（全源最短路径） 中间节点逐步优化所有节点对之间的最短路径。

————

##### 最小生成树是指在一个**连通无向带权图**中，找到一个边的子集，使得：

1. ##### 所有顶点都连通

2. ##### 没有环（形成树结构）

3. ##### 所有边的权重之和最小

##### Prim 可以确定起始点

##### 有权图Prim, 无权图BFS

##### Kruskal 不需要指定起始点