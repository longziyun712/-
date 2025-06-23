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
parent=list(range(n+1))  #这是从0到n，不然没有n了
total=[1]*(n+1)          # 多取一个
for _ in range(m):
    a,b=list(map(int,input().split()))
    union(a,b)

classes = [total[x] for x in range(1, n + 1) if x == parent[x]]
                                #从1开始 把0抛出掉，因为没有0这个同学
print(len(classes))
print(' '.join(map(str, sorted(classes, reverse=True))))

