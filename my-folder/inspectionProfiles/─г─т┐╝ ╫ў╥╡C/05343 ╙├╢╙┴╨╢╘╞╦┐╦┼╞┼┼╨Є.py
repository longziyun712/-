n=int(input())
lst=input().split()
Queue1=[]
Queue2=[]
Queue3=[]
Queue4=[]
Queue5=[]
Queue6=[]
Queue7=[]
Queue8=[]
Queue9=[]
for x in lst:
    if x[1]=='1':
        Queue1+=[x]
    if x[1]=='2':
        Queue2+=[x]
    if x[1]=='3':
        Queue3+=[x]
    if x[1]=='4':
        Queue4+=[x]
    if x[1]=='5':
        Queue5+=[x]
    if x[1]=='6':
        Queue6+=[x]
    if x[1]=='7':
        Queue7+=[x]
    if x[1]=='8':
        Queue8+=[x]
    if x[1]=='9':
        Queue9+=[x]

print('Queue1:'+' '.join(Queue1))
print('Queue2:'+' '.join(Queue2))
print('Queue3:'+' '.join(Queue3))
print('Queue4:'+' '.join(Queue4))
print('Queue5:'+' '.join(Queue5))
print('Queue6:'+' '.join(Queue6))
print('Queue7:'+' '.join(Queue7))
print('Queue8:'+' '.join(Queue8))
print('Queue9:'+' '.join(Queue9))

QueueA=[]
QueueB=[]
QueueC=[]
QueueD=[]
Queue=Queue1+Queue2+Queue3+Queue4+Queue5+Queue6+Queue7+Queue8+Queue9

for x in Queue:
    if x[0]=='A':
        QueueA+=[x]
    if x[0]=='B':
        QueueB+=[x]
    if x[0]=='C':
        QueueC+=[x]
    if x[0]=='D':
        QueueD+=[x]
print('QueueA:'+' '.join(QueueA))
print('QueueB:'+' '.join(QueueB))
print('QueueC:'+' '.join(QueueC))
print('QueueD:'+' '.join(QueueD))
print(' '.join(QueueA+QueueB+QueueC+QueueD))



from collections import deque
n = int(input())
queues = [deque() for _ in range(9)]
cards = deque(list(input().split()))

while cards:
    card = cards.popleft()
    queues[int(card[1])-1].append(card)

qs = {'A': deque(), 'B': deque(), 'C': deque(), 'D': deque()}
for i in range(9):
    tmp = []
    while queues[i]:
        card = queues[i].popleft()
        qs[card[0]].append(card)
        tmp.append(card)
    print(f'Queue{i+1}:'+' '.join(tmp))

result = []
for char in qs.keys():
    tmp = []
    while qs[char]:
        card = qs[char].popleft()
        result.append(card)
        tmp.append(card)
    print(f'Queue{char}:' + ' '.join(tmp))
print(*result)







