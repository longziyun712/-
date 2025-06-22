from collections import deque
n=int(input())
lst=deque(input().split())
queues=[deque() for _ in range(9)]
while lst:
    factor=lst.popleft()
    queues[int(factor[1])-1].append(factor)
for i in range(9):
    print(f'Queue{i+1}:'+' '.join(queues[i]))

dict={'A':deque(),'B':deque(),'C':deque(),'D':deque(),}
result = []
for i in range(9):
    result=[]
    while  queues[i]:
        fac=queues[i].popleft()
        dict[fac[0]].append(fac)
        result+=[fac]
        print(result)
for n in dict.keys():
    print(f'Queue{n}:'+' '.join(dict[n]))
print(result)




'''

from collections import deque
n=int(input())
lst=deque(input().split())
queues=[deque() for _ in range(9)]
while lst:
    factor=lst.popleft()
    queues[int(factor[1])-1].append(factor)
for i in range(9):
    print(f'Queue{i+1}:'+' '.join(queues[i]))

dict={'A':deque(),'B':deque(),'C':deque(),'D':deque(),}
result = []
for i in range(9):

    while  queues[i]:
        fac=queues[i].popleft()
        dict[fac[0]].append(fac)
for n in dict.keys():
    result+=[i for i in dict[n]]
    print(f'Queue{n}:'+' '.join(dict[n]))
print(*result)

'''





'''
from collections import deque
n=int(input())
lst=input().split()
d=[deque() for _ in range(9)]
for i in lst:
    d[int(i[1])-1].append(i)
for j in range(9):
    print(f'Queue{j+1}:'+' '.join(d[j]))
result=[]
dict={'A':deque(),'B':deque(),'C':deque(),'D':deque(),}
for m in d:
    for s in m:
        dict[s[0]].append(s)
for n in dict.keys():
    result+=[i for i in dict[n]]
    print(f'Queue{n}:'+' '.join(dict[n]))
print(*result)'''