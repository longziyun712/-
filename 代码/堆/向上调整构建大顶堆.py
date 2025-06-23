#向上调整：和父节点比较  建堆：从索引 1 开始
n=int(input())
lst=list(map(int,input().split()))

for i in range(n):
    while i>=0:
        if (i-1)//2>=0 and lst[(i-1)//2]<lst[i]:
            lst[(i-1)//2],lst[i]=lst[i],lst[(i-1)//2]
            i=(i-1)//2
        else:
            break
print(*lst)