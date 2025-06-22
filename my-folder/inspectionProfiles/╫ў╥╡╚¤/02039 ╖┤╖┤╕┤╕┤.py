n=int(input())
s=input()
m=len(s)//n
lst=[]
s1=''
for i in range(m):
    if i%2==0: #取余数
        lst+=[list(s[n*i:n*(i+1)])]
    else:
        lst+=[list(s[n*(i+1)-1:n*i-1:-1])]  # 倒过来但是不对了 【0:5）和（10:5；-1】遍历出错
for i in range(n):
    for j in range(m):
        s1+=lst[j][i]
print(s1)
