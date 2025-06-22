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
        return True
    else:
        return False
n,m=map(int,input().split())
parent=list(range(n+1))  #这是从0到n，不然没有n了
total=[1]*(n)          # 多取一个
x=0
for _ in range(m):
    a,b=list(map(int,input().split()))
    if not union(a,b):
        x=1
size=[i for i in range(n) if parent[i]==i]

if len(size)==1:
    print('connected:yes')
else:
    print('connected:no')
if x==1:
    print('loop:yes')
else:
    print('loop:no')