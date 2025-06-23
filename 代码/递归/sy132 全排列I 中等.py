maxn = 11
hashTable = [False] * maxn  # 当整数i已经在数组 P中时为 true

#@recviz
def increasing_permutaions(n, prefix=[]):
    if len(prefix) == n:  # 递归边界，已经处理完排列的1~位
        return [prefix]

    result = []
    for i in range(1, n + 1):
        if hashTable[i]:
            continue

        hashTable[i] = True  # 记i已在prefix中
        # 把i加入当前排列，处理排列的后续号位
        result += increasing_permutaions(n, prefix + [i])
        hashTable[i] = False  # 处理完为i的子问题，还原状态

    return result


n = int(input())
result = increasing_permutaions(n)
for r in result:
    print(' '.join(map(str,r)))