def insert_hash_table(keys, M):
    table = [0.5] * M  # 用 0.5 表示空位
    result = []
    for key in keys:
        index = key % M
        i = index
        while True:
            if table[i] == 0.5 or table[i] == key:
                result.append(i)
                table[i] = key
                break
            i = (i + 1) % M
    return result
# 使用标准输入读取数据
import sys
input = sys.stdin.read
data = input().split()
N = int(data[0])
M = int(data[1])
keys = list(map(int, data[2:2 + N]))
positions = insert_hash_table(keys, M)
print(*positions)


# 2200015507 王一粟
# n, m = map(int, input().split())
# num_list = [int(i) for i in input().split()]
import sys
input = sys.stdin.read
data = input().split()
index = 0
n = int(data[index])
index += 1
m = int(data[index])
index += 1
num_list = [int(i) for i in data[index:index+n]]
mylist = [0.5] * m
def generate_result():
    for num in num_list:
        pos = num % m
        current = mylist[pos]
        if current == 0.5 or current == num:
            mylist[pos] = num
            yield pos
        else:
            sign = 1
            cnt = 1
            while True:
                now = pos + sign * (cnt ** 2)
                current = mylist[now % m]
                if current == 0.5 or current == num:
                    mylist[now % m] = num
                    yield now % m
                    break
                sign *= -1
                if sign == 1:
                    cnt += 1
result = generate_result()
print(*result)