n=int(input())
a=list(map(int,input().split()))
M = int(input())
i,j=0,n-1
while i<j:
    if a[i]+a[j]==M:
        print(a[i],a[j])
        i+=1
        j-=1
    elif a[i]+a[j]<M:
        i+=1
    elif a[i] + a[j] < M:
        j-=1
