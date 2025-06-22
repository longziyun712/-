Arow,Acol=map(int,input().split())
A=[]
for i in range(Arow):
    A+=[[int(x) for x in input().split()]]

Brow,Bcol=map(int,input().split())
B=[]
for i in range(Brow):
    B+=[[int(x) for x in input().split()]]

Crow,Ccol=map(int,input().split())
C=[]
for i in range(Crow):
    C+=[[int(x) for x in input().split()]]

if Acol==Brow and (Arow,Bcol)==(Crow,Ccol):
    D=[[0]*Bcol for i in range(Arow)]  # 创建都是0的矩阵
    for i in range(Arow):
        for j in range(Bcol):
            D[i][j]+=sum(A[i][m]*B[m][j] for m in range(Acol))+C[i][j]
        print(' '.join(map(str,D[i])))
else:
    print('Error!')
