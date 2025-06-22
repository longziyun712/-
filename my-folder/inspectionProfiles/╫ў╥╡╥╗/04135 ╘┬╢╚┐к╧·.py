n,m=[int(x) for x in (input().split())]
lst=[]
for i in range(n):
    lst+=[int(input())] # 或者lst.append(int(input().strip()))
left,right=max(lst),sum(lst)

while left < right:
    sum=0
    num=1
    mid=(left+right)//2
    for i in lst:
        if i + sum<=mid:
            sum+=i #没超过就继续累加sum
        else:
            num+=1
            sum=i #超过了，多建一组，重新累加
    if num<=m:
        right=mid
    else:
        left=mid+1
result=right
print(result)

