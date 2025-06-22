
while True:
    N,M=map(int,input().split())
    if N==0 and M==0:
        break

    from collections import defaultdict
    dct=defaultdict(int)
    for i in range(N):
        lst=list(map(int,input().split()))
        for j in lst:
            dct[j]+=1
    result=[]
    for m in sorted(dct.keys()):
        if dct[m]==sorted(dct.values(), reverse=True)[1]:
            result+=[m]
    print(*result)
'''
    lst = []
    for i in range(N):
        lst+=list(map(int,input().split()))
        for j in lst:
            dct[j]+=1
            print(lst)
这么写上一行的list会被加进去 
'''
''' 优化： 避免for 循环里 多次排序调用 
eg sorted() 如果数字都相同 ，会报错！！！
    sorted_values = sorted(set(dct.values()), reverse=True)
    if len(sorted_values) < 2:
        second_highest = sorted_values[0]
    else:
        second_highest = sorted_values[1]

'''