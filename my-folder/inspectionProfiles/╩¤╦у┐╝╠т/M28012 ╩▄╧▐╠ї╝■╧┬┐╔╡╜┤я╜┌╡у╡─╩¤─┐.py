def find(a):
    if parent[a]!=a:
        parent[a]=find(parent[a])
    return parent[a]
def union(a,b):
    p=find(a)
    q=find(b)

    parent[p] = q
    total[q] += total[p]

n=int(input())
lst=[]
parent=list(range(n+1))
total=[1]*(n+1)
for _ in range(n-1): ##多写了一条边
    lst.append(tuple(map(int,input().split())))
limit=list(map(int,input().split()))
for (a,b) in lst:
    if a not in limit and b not in limit:
        union(a,b)
    else:
        continue
print(total[find(0)])
