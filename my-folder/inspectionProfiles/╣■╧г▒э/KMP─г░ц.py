def build_next(pattern):
    next = [0] * len(pattern)
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = next[j - 1]  #退回未匹配时候 重新计算next中的前后缀长度
        if pattern[i] == pattern[j]:
            j += 1
        next[i] = j
    return next
def kmp_search(text, pattern):
    next = build_next(pattern)
    j = 0
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = next[j - 1]
        if text[i] == pattern[j]:
            j += 1
        if j == len(pattern):
            print(f"Found at index {i - j + 1}")
            j = next[j - 1]
# 示例
text = "ABCABDABCABE"
pattern = "ABCABE"
kmp_search(text, pattern)  # 输出: Found at index 6


'''
gpt
这是一个字符串匹配问题，通常使用KMP算法（Knuth-Morris-Pratt算法）来解决。
使用了 Knuth-Morris-Pratt 算法来寻找字符串的所有前缀，并检查它们是否由重复的子串组成，
如果是的话，就打印出前缀的长度和最大重复次数。
'''

# 得到字符串s的前缀值列表
def kmp_next(s):
  	# kmp算法计算最长相等前后缀
    next = [0] * len(s)
    j = 0
    for i in range(1, len(s)):
        while s[i] != s[j] and j > 0:
            j = next[j - 1]
        if s[i] == s[j]:
            j += 1
        next[i] = j
    return next


def main():
    case = 0
    while True:
        n = int(input().strip())
        if n == 0:
            break
        s = input().strip()
        case += 1
        print("Test case #{}".format(case))
        next = kmp_next(s)
        for i in range(2, len(s) + 1):
            k = i - next[i - 1]		# 可能的重复子串的长度
            if (i % k == 0) and i // k > 1:
                print(i, i // k)
        print()


if __name__ == "__main__":
    main()
