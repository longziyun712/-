n=int(input())
lst=list(map(int,input().split()))
import heapq
heapq.heapify(lst)
res=0
while len(lst)>1:
    a=heapq.heappop(lst)
    b=heapq.heappop(lst)
    add=a+b
    res+=add
    heapq.heappush(lst,add)
print(res)

