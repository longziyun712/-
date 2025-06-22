 # 题目理解：这个题读题都没读明白…………“M表示查询的数目”，这句话说的就很奇怪：查询什么的数目？
 # 希望以后题目描能从读题者的视角多说一些 也就更有可能说清楚
#比如本题，“接下来M行每行N个数，每个数表示这个词要不要出现，1表示出现，-1表示不出现，0表示无所谓。数据保证每行至少出现一个1。”
#加上一句，“这是针对文档中词汇是否出现的查询条件”就会好很多。
from collections import defaultdict
N=int(input())
dct=defaultdict(list)
s=set()  ## 创建集合唯一方式
for i in range(N):  # 把词汇诸如ABC编成了0 1 2 …… N-1
    doc=list(map(int,input().split()))  #一定要全部转成整数！！！
    dct[i]=doc[1:]
    for j in doc[1:]:
        s.add(j)
dct2=defaultdict(list)
for i in s:
    for j in range(N):
        if i in dct[j]:
            dct2[i]+=[j]

M=int(input())
for i in range(M):
    lst=list(map(int,input().split()))  ##这里是字符串！！！！ 要转成数字 才能比 1 -1 0
    result=[]
    for j in s:
        n = 0
        for x in range(N):  # N个词汇
            if (lst[x]==1 and x in dct2[j]) or (lst[x]==-1 and x not in dct2[j]) or lst[x]==0:
                continue
            else:
                n+=1
        if n ==0:
            result+=[j]
    if result==[]:
        print('NOT FOUND')
    else:
        print(*sorted(result))
#三重循环 超时了 放弃吧！
#RE (Runtime Error)：程序异常终止，通常是代码错误（如类型错误）导致。
#TLE (Time Limit Exceeded)：程序正常运行但超时，通常是算法效率问题或死循环导致。