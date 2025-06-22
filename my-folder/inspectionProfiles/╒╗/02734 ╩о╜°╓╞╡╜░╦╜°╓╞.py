a=int(input())
if a==0:
    print(a)
else:
    stack=[]
    while a>0:
        stack.append(a%8)
        a=a//8
    result=''
    while stack:
        result+=str(stack.pop())
    print(result)