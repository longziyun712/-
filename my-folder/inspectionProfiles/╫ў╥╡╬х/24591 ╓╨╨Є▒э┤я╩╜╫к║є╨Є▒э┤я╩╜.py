n=int(input())
for _ in range(n):
    s = input()  #s = input().replace(" ", "")  # 去掉空格
    stack=[]
    help=[]
    dct={'+':1,'-':1,'*':2,'/':2}
    i=0
    while i <len(s):
        if s[i]=='(':
            help.append(s[i])
        elif s[i] == ')':
            while help[-1] != '(':
                stack.append(help.pop())
            help.pop()
        elif s[i] in'+-*/':
            while help and help[-1]!='(' and dct[s[i]]<=dct[help[-1]] and help[-1]!='(':
                # dct[s[i]]<=dct[help[-1]]要有等号，保证从先往后的顺序一致性 eg(3)*((3+4)*(2+3.5)/(4+5)) 应该先乘后除
                stack.append(help.pop())
            help.append(s[i])
        else:
            num=[]
            while i<len(s) and (s[i].isdigit() or s[i]=='.'): # 处理数字和浮点数
                num.append(s[i])
                i+=1
            stack.append(''.join(num))
            continue
        i+=1
    while help:
        stack.append(help.pop())
    print(*stack)
### 原理 7*8+3——7 8 * 3 + 前面的先执行，那就先弹出来到stack
### 7+8*3——7 8 3 * + 后面的先执行 没问题 因为*会先弹出来