from collections import deque
n, m = map(int, input().split())
lst=list(map(int, input().split()))
adjlist = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adjlist[u].append(v)
    adjlist[v].append(u)
visited = [False] * n
def dfs(node,res):
    visited[node]=True
    res+=lst[node]
    for i in adjlist[node]:
        if not visited[i]:
            res+=dfs(i,0)
    return res
result=[]
for i in range(n):
    if not visited[i]:
        result.append(dfs(i,0))
print(max(result))
