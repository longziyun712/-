d=int(input())
n=int(input())
from collections import defaultdict
dct=defaultdict(int)
for t in range(n):
    x,y,i=list(map(int,input().split()))
    dct[(x,y)]=i
bomb=defaultdict(int)
for (i,j) in list(dct):# 必须加list
    for p in range(max(i-d,0),min(1025,i+d+1)):  # 边界约束一下
        for q in range(max(j-d,0),min(1025,j+d+1)):
            bomb[(p,q)]+=dct[(i,j)]
num=0
r=max(bomb.values())
for (x,y) in list(bomb.keys()):
    if bomb[(x,y)]==r:
        num+=1
print(num,r)
'''
for s in range(p - d, p + d + 1):
    for m in range(q - d, q + d + 1):
        bomb[(p, q)] += dct[(s, m)]
循环太多，有重复！！！！
'''