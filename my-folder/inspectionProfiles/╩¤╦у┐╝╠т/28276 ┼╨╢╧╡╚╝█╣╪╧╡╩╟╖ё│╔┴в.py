def find(a):
    if parent[a]!=a:
        parent[a]=find(parent[a])
    return parent[a]
def union(a,b):
    p=find(a)
    q=find(b)
    if p!=q:
        if size[p]>size[q]:
            parent[q]=p
            size[p]+=size[q]
        else:
            parent[p] = q
            size[q] += size[p]
parent=list(range(1000))
size=[1]*1000
lst=[]
n=int(input())
from collections import defaultdict
alpha=defaultdict()
sss=set()
i=0
j=1000
for _ in range(n):
    i+=1
    j-=1
    s=input()
    a=s[0]
    b=s[3]
    if a not in alpha.keys():
        alpha[a]=i
    if b not in alpha.keys():
        alpha[b]=j
    if s[1]=='=':
        union(alpha[a],alpha[b])
        sss.add(a)
        sss.add(b)
    else:
        lst+=[(a,b)]
res=True
for a,b in lst:
    if a not in sss and b not in sss:
        continue
    if find(alpha[a])==find(alpha[b]):
        res=False
        break
print(res)

