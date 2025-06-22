n,m=map(int,input().split())
lst=list(map(int,input().split()))
num=[i for i in range(1,n+1)]
while len(lst)!=1:
    if lst[0]<=m:
        lst.pop(0)
        num.pop(0)
    else:
        lst.append(lst.pop(0)-m)
        num.append(num.pop(0))
print(num[0])
