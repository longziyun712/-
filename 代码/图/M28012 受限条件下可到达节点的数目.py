from collections import defaultdict, deque
class Graph:
    def __init__(self):
        self.adjlist=defaultdict(list)
    def addEdge(self,u,v):
        self.adjlist[u].append(v)
        self.adjlist[v].append(u)
    def bfs(self,node,res):
        queue=deque()
        visited=set()
        queue.append(node)
        visited.add(node)
        while queue:
            a=queue.popleft()
            res+=1
            for i in self.adjlist[a]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        return res
n=int(input())
graph=Graph()
lst1=[]
for i in range(n-1):
    lst1.append(list(map(int,input().split())))
lst=list(map(int,input().split()))
for l in lst1:
    if l[0] not in lst and l[1] not in lst:
        graph.addEdge(l[0],l[1])
print(graph.bfs(0,0))