m,n=[int(x) for x in input().split()]
lst=[]
for _ in range(m):
    lst+=[int(input())]
left,right=1,max(lst)
result=0
while left<=right:   # =等号 检查left=right的情况
    mid=(left+right)//2
    y=0
    for x in lst:
        y+=x//mid
    if y>=n:
        result=mid
        left=mid+1    # +1  都是为了跳出循环
    else:
        right=mid-1   # -1
print(result)

