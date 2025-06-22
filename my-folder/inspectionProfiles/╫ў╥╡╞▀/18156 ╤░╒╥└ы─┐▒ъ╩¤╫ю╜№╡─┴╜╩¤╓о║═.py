n=int(input())
lst=sorted([int(x) for x in input().split()])
left ,right= 0,len(lst)-1
cha=n
result=0
while left<right:
    sum=lst[left]+lst[right]
    if abs(sum-n)<cha:
        cha=abs(sum-n)
        result=sum
    elif abs(sum-n)==cha:
        if sum<result:
            result=sum
    if sum<=n:
        left+=1
    else:
        right-=1
print(result)
