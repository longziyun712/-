n,c=map(int,input().split())
lst=[]
for _ in range(n):
    lst+=[int(input())]
l=0
r=max(lst)
lst.sort()
result=max(lst)
while l<=r:
    mid=(l+r)//2
    m=1 #计数
    pre=0 #前一个的位置
    for i in range(1,n):
        if lst[i]-lst[pre]>=mid:
            m+=1
            pre=i
        else:
            continue
    if m >=c:
        l=mid+1
        result=mid   #取结果一定要在可行的部分取 在可行的情况下取最值
    else:
        r = mid - 1
print(result)