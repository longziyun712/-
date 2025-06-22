while True:
    try:
        s=input().strip() #开头有空格
    except EOFError:
        break
    #换个思路
    n=s.count('@')
    m = s.find('@')
    if n!=1:
        print('NO')
    elif '@'==s[0] or '@'==s[-1] or '.'==s[0] or '.'==s[-1]:
        print('NO')
    elif '@.' in s or '.@' in s:
# 题目：'@'之后至少要有一个'.'，并且'@'不能和'.'直接相连 直接被误导 去查了‘@.' 但实际上还有‘.@’的情况没检查，弄了好久好久才查出来。
# 方法：最后一定要一个逗号一个逗号排除！！！！！！保证满足所有的条件
        print('NO')
    elif s[m+1:].count('.')<1: #至少有一个，不是只有一个  s.count(s[m+1:])怎么count都是1
        print('NO')
    else:
        print('YES')

    '''想简单了并不能过…………
    n=s.count('@')
    p=s.find('@')
    q=s.rfind('.')
    m=s.find('.')
    x=s.find(',',p)
    
    if (n!=1 or p==0 or p==len(s)-1
            or m==0 or q==len(s)-1 or q<=p+1): 
        print('NO')
                  #q<=p+1 不能完全判断呜呜呜 因为@后面可能有两个'.'
    if (n!=1 or p==0 or p==len(s)-1
            or m==0 or q==len(s)-1 or q<=p+1 or s[p+1]=='.' or len(str(x))!=1):
        print('NO')
    else:
        print('YES')
    print(x)
    '''