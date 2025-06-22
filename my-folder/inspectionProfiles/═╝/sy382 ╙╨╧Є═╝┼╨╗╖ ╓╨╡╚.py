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
