import heapq
n=int(input())
lst=list(map(int,input().split()))
heapq.heapify(lst)
res=0
while len(lst)>1:
    a=heapq.heappop(lst)
    b=heapq.heappop(lst)
    he=a+b
    res+=he
    heapq.heappush(lst,he)
print(res)