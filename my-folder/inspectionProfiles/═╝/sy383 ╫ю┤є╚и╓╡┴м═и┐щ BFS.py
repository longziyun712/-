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

