m=int(input())
lst=[i for i in range(m)]
def count(stack,lst):
    n=0
    if stack:
        n+=count(stack[:-1],lst)
    if lst:
        n+=count(stack+[lst[0]],lst[1:])
    if len(stack)==1 and not lst:
        n=1
    return n
print(count([],lst))