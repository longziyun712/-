m=int(input())
for _ in range(m):
    n=int(input())
    stack=[]
    queue=[]
    s = 1
    for __ in range(n):
        lst=input().split()
        if lst[0]=='push':
            stack.append(lst[1])
            queue.append(lst[1])
        else:
            if stack and queue:
                stack.pop()
                queue.pop(0)
            else:
                s=0
#  这里最开始是break然后直接命名queue和stack了 但是后续数据没有完整接收
#  导致最后应该有数据没有被读入！！！！牛牛牛
    if s==0:
        print('error','error',sep='\n')
    else:
        print(' '.join(queue))
        print(' '.join(stack))
