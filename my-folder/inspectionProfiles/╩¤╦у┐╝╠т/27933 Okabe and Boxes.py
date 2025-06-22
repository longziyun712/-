n=int(input())
a=[]
res=0
remove=0
for _ in range(2*n):
    lst=input().split()
    if len(lst)==2:
        a.append(int(lst[1]))
    else:
        remove+=1
        if a[-1]!=remove:
            a.sort(reverse=True)
            res+=1
        a.pop()
print(res)

