A=list(map(int,input().split()))
B=list(map(int,input().split()))
C=[]
i,j=0,0
while i<len(A) and j<len(B):
    if A[i]>=B[j]:
        C.append(B[j])
        j+=1
    else:
        C.append(A[i])
        i+=1
C.extend(A[i:])  #连接列表用extend
C.extend(B[j:])
print(C)