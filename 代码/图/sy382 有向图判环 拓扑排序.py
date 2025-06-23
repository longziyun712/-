from collections import deque,defaultdict
n, m = map(int, input().split())
adjlist = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adjlist[u].append(v)
def topological_sort(adjlist):
    indegree = defaultdict(int)
    result = []
    queue = deque()
    # 计算每个顶点的入度
    for u in range(len(adjlist)):
        for v in adjlist[u]:
            indegree[v] += 1
    # 将入度为 0 的顶点加入队列
    for u in range(len(adjlist)):
        if indegree[u] == 0:
            queue.append(u)
    # 执行拓扑排序
    while queue:
        u = queue.popleft()
        result.append(u)
        for v in adjlist[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)
    # 检查是否存在环
    if len(result) == len(adjlist):
        return 'No'
    else:
        return 'Yes'
print(topological_sort(adjlist))