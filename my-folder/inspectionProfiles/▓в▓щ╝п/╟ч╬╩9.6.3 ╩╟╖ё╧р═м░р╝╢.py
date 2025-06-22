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
k=int(input())
for i in range(k):
    a,b=map(int,input().split())
    if find(a)==find(b):
        print('Yes')
    else:
        print('No')
