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
        lst[p-1]=max(lst[p-1],lst[q-1])  #把班级根节点的成绩改成班级最大值去
n,m=map(int,input().split())
lst=list(map(int,input().split()))
parent=list(range(n+1))
total=[1]*(n+1)

for i in range(m):
    a,b=map(int,input().split())
    union(a,b)

root_count = 0
for i in range(1, n + 1):
    if parent[i] == i:
        root_count += 1

scores=[lst[find(a)-1] for a in range(1,n+1) if a==parent[a]] #提取根节点的成绩
print(root_count)
scores.sort(reverse=True)
print(*scores)
