n=int(input())
for _ in range(n):
    lst=input().split()
    stack=[]
    for s in lst:
        if s.isnumeric() or '.'in s :
            stack.append(float(s))

        else:
            b=stack.pop()
            a=stack.pop()
            if s=='+':
                stack.append(a+b)
            if s=='-':
                stack.append(a-b)
            if s=='*':
                stack.append(a*b)
            if s=='/':
                stack.append(a/b)
    print('%.2f'% float(stack[0]))

