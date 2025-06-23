from collections import deque
n,m,s,k=list(map(int, input().split()))
adjlist = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    adjlist[u].append(v)

def bfs(node,res,n):
    visited[node]=0
    queue=deque()
    queue.append(node)
    while queue:
        a=queue.popleft()
        for i in adjlist[a]:
            if visited[i]==100:
                queue.append(i)
                visited[i]=visited[a]+1
    return visited
visited=[100]*(n)
lst=[i for i in bfs(s,0,_)if i <= k]
print(len(lst))

