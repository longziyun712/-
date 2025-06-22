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
n,m=map(int,input().split())
parent=list(range(n+1))
total=[1]*(n+1)
for i in range(m):
    a,b=map(int,input().split())
    union(a,b)

root_count = 0
for i in range(1, n + 1):
    if parent[i] == i:
        root_count += 1

if root_count == 1:
    print('Yes')
else:
    print('No')