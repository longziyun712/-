m,n,p,q=map(int,input().split())
M=[]
K=[]
for i in range(m):
    M+=[[int(x) for x in input().split()]]
for i in range(p):
    K+=[[int(x) for x in input().split()]]
R=[[0]*(n-q+1) for i in range(m-p+1)]
for i in range(m-p+1):
    for j in range(n-q+1):
        for x in range(i,i+p): # 不是 i+p-1 因为 i+p-1取不到 （range是左闭右开）
            R[i][j]+=sum(M[x][y]*K[x-i][y-j] for y in range(j,j+q))
for z in R:
    print(' '.join(map(str,z)))