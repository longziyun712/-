n=int(input())
for _ in range(n):
    m = int(input())
    lst = []
    for __ in range(m):
        a,b=map(int,input().split())
        if a==1:
            lst.append(b)
        else:
            if b==0:
                lst.pop(0)
            else:
                lst.pop()
    if lst:
        print(*lst)
    else:
        print('NULL')
