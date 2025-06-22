from collections import defaultdict as dt
n=int(input())
dct=dt(list)
for i in range(n):
    model,para=input().split('-')
    if para[-1]=='M':
        dct[model].append((para,float(para[:-1])))
        #也要转成数字！不然是字符串排序
        #append其实调用的是列表的函数
    elif para[-1]=='B':
        dct[model].append((para,float(para[:-1])*1000))

for i in sorted(dct.keys()):
    paras=sorted(dct[i],key=lambda x:x[1])
    print(f'{i}:',', '.join(map(lambda x:x[0],paras)))
    #'也可写为', '.join(f[0] for f in paras)