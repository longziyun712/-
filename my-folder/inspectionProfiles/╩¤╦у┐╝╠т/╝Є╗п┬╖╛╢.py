s=input()
stack=[]
for i in s:
    if i != '.':
        if stack and stack[-1] == '.' and len(stack)>1 and stack[-2] != '.': # 1
            while stack[-1] != '/':
                stack.pop()
            continue
        if stack and stack[-1] == '.' and len(stack) > 2 and stack[-2] == '.' and stack[-3] == '.':  # 3
            stack.append(i)
            continue
        if stack and stack[-1] == '.' and len(stack)>2 and stack[-2] == '.' : #2
            while stack[-1] != '/':
                stack.pop()
            stack.pop()
            while stack and stack[-1] != '/':
                stack.pop()
    stack.append(i)
    if i=='/':
        if len(stack)>1 and stack[-2]=='/':
            stack.pop()
        else:
            continue

if stack[-1]=='/':
    stack.pop()
if stack==[]:
    stack.append('/')
print(''.join(stack))

#and stack[-3]!='.' or len(stack)==2 and stack[-2] == '.' )