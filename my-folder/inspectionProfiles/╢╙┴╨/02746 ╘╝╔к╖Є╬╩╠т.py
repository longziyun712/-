while True:
    a,b=map(int,input().split())
    if a==0 and b==0:
        break
    lst=[i for i in range(1,a+1)]
    while len(lst)!=1:
        for j in range(b-1):
            lst.append(lst.pop(0))
        lst.pop(0)
    print(int(lst[0]))


