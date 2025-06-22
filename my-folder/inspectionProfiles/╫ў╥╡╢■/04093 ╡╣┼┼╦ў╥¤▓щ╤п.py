from collections import defaultdict
N=int(input())
dct=defaultdict(list)
s=set()  ## 创建集合唯一方式
for i in range(N):  # 把词汇诸如ABC编成了0 1 2 …… N-1
    doc=list(map(int,input().split()))  #一定要全部转成整数！！！
    dct[i]=doc[1:]
    for j in doc[1:]:
        s.add(j)
M=int(input())
for i in range(M):
    lst=list(map(int,input().split()))  ##这里是字符串！！！！ 要转成数字 才能比 1 -1 0
    s1 = s.copy()
    #唯一初始化方法 通过每次在集合里增加和删减，减少遍历集合的时间复杂度。核心*****
    for x in range(N):
        if lst[x]==1:
            s1&=set(dct[x])  # 集合的交集符号 必须先交后减
        elif lst[x]==-1:
            s1-= set(dct[x]) # 左边集合去掉右边集合的元素
    if s1==set():
        print('NOT FOUND')
    else:
        print(*sorted(s1))

#RE (Runtime Error)：程序异常终止，通常是代码错误（如类型错误）导致。
#TLE (Time Limit Exceeded)：程序正常运行但超时，通常是算法效率问题或死循环导致。