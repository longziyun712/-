s=input()
stack=[]
for x in s:
    stack.append(x)
    if x ==']':
        stack.pop()
        helpstack=[]
        while stack[-1]!='[':
            helpstack.append(stack.pop())
        stack.pop()
        result = ''
        while helpstack[-1] in '0123456789':
            result+=helpstack.pop()
        helpstack=helpstack*int(result) #保证helpstack还是列表/栈
        while helpstack!=[]:
            stack.append(helpstack.pop())
print(*stack,sep='')

















































