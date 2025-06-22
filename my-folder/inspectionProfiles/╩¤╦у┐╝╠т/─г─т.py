n,m=list(map(int,input().split()))
lst=set(range(n+1))
for _ in range(m):
    a,b=list(map(int,input().split()))
    for i in range(a,b+1):
        if i in lst:
            lst.remove(i)
print(len(lst))
