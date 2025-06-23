from collections import defaultdict #为缺失键自动创建
n,k=map(int,input().split())
dic=defaultdict()
for i in range(1,n+1):
    dic[i]=list(map(int,input().split()))
d=dict(sorted(dic.items(),key=lambda x:x[1][0],reverse=True)[:k]) #sorted是列表
n=sorted(d.items(),key=lambda x:x[1][1],reverse=True)[0][0]
print(n)
