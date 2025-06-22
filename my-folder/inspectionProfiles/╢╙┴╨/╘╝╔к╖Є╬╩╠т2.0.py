from collections import deque
while True:
    n,p,m=list(map(int,input().split()))
    if n==0 and m==0 and p==0:
        break
    queue=deque([i for i in range(1,n+1)])
    lst=[]
    for i in range(p-1):
        queue.append(queue.popleft())
    while queue:
        for i in range(m-1):
            queue.append(queue.popleft())
        lst.append(queue.popleft())
    print(','.join(map(str,lst)))
