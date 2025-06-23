import math
while True:
    a,b,c,d,e,f=map(int,input().split())
    if a==b==c==d==e==f==0:
        break
    n=0
    n+=f
    n+=e
    n+=d #5个2*2
    n+=math.ceil(c/4)
    m=c%4 if c%4!=0 else 3.5  #这里取0就错了!
    if b>5*d+(7-2*m):  #计算2*2
        n+=math.ceil((b-5*d-(7-2*m))/9)
    if a>36*n-36*f-25*e-16*d-9*c-4*b: #1*1排除法
        n+=math.ceil((a-(36*n-36*f-25*e-16*d-9*c-4*b))/36)
    print(n)


#math.ceil(x) 	向上取整
#int(x) 直接截断小数
#x // 1 向下取整