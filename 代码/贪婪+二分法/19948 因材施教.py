n,m=map(int,input().split())
lst=list(map(int,input().split()))
lst.sort()    #lst=lst.sort()会返回None
cha={}
for i in range(n-1):
    cha[i]=lst[i+1]-lst[i]
chazhi=sorted(cha.items(),key=lambda x:x[1],reverse=True)
elect=[]
for j in range(m-1):
    elect+=[chazhi[j][0]]
d=max(lst)-min(lst)
for x in elect:
    d-=lst[x+1]-lst[x]
print(d)
