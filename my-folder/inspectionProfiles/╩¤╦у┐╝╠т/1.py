s=input()
res=''
c=0
for i in s:
    c=(c*2+int(i))%5
    if c==0:
        res+='1'
    else:
        res+='0'
print(res)
