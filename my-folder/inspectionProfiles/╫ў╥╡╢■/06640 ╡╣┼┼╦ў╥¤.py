from collections import defaultdict
N=int(input())
dct=defaultdict(list)
'''
for i in range(N):
    a=int(input())
    for j in range(a):
        dct[i]=[input().split()]
不可以 因为input读取的是整行
'''
for i in range(N):
    doc=input().split() #默认是list
    dct[i]=doc[1:]
M=int(input())
for i in range(M):
    word=input()
    lst=[]
    for j in range(N):
        if word in dct[j]:
            lst+=[j+1]  ##+1是因为电脑索引从0开始 题目从1开始
    if lst!=[]:
        print(*lst)  #打印列表
    else:
        print('NOT FOUND')