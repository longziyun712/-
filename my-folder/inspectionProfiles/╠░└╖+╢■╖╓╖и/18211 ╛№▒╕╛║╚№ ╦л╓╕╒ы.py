n=int(input())
lst=list(map(int,input().split()))
lst.sort()
l=0
re=0
r=len(lst)-1
while l<=r:
    if lst[l]<=n:
        re+=1
        n-=lst[l]
        l+=1
    elif l==r:
        break
    else:
        if re==0:
            break
        else:
            re-=1
            n += lst[r]
            r-=1
print(re)
