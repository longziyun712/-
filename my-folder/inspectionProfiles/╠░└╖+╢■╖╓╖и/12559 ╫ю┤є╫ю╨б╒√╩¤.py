'''n=int(input())
lst=input().split()
lst.sort(key=lambda x:x*3)  ## *3能对是因为碰巧
max=''
min=''
for i in range(n):
    min+=lst[i]
for j in range(n):
    max+=lst[-j-1]
print(max,min)

#输入3
#3 34 302
# #结果343023 330234 字典序会优先把1位数算成小的
'''

#类似冒泡排序 把3排在30后面
n=int(input())
lst=input().split()
for i in range(n-1):
    for j in range(i+1,n):
        if lst[i]+lst[j]<lst[j]+lst[i]:
            continue
        else:
            lst[i],lst[j]=lst[j],lst[i]
max=''
min=''
for i in range(n):
    min+=lst[i]
for j in range(n):
    max+=lst[-j-1]
print(max,min)



'''冒泡排序
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):          # 固定执行 n-1 轮
        for j in range(n - 1 - i):  # 每轮比较次数递减
            if arr[j] > arr[j + 1]: # 前大于后则交换
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# 测试
arr = [64, 34, 25, 12, 22, 11, 90]
print(bubble_sort(arr))  # 输出: [11, 12, 22, 25, 34, 64, 90]
'''