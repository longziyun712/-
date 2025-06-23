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

