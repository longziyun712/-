lines = []
while True:  #oj提交使用
    try:
        lines.append(input())
    except EOFError:
        break
# 输入方式2：空行终止 pc运行使用
while True:
    line = input().strip()
    if line == "":
        break
    lines.append(line)
for j in lines:
    stack=[]
    mark=[]
    for i in range(len(j)):
        if j[i] =='(':
            stack.append(i)
            mark+=' '
        elif j[i] ==')':
            if not stack:
                mark+='?'
            else:
                stack.pop()
                mark+=' '
        else:
            mark+=' '
    for m in stack:
        mark[m]='$'
    print(j)
    print(''.join(mark))
#这个输入也好用
'''
import sys

for line in sys.stdin:
    num = line.strip()'''