st=input()
stack=[]
for i,s in enumerate(st):
    help=[]
    if s==']':
        while stack[-1]!='[':
            help.append(stack.pop())
        stack.pop()
        res = ''
        while help[-1] in '0123456789':
            res += help.pop()
            print(help)
        help=help*int(res)
        while help:
            stack.append(help.pop())
    else:
        stack.append(s)
print(*stack,sep='')