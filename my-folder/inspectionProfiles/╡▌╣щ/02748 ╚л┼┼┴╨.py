def permute(s):
    if len(s) == 1:
        return [s]
    res = []
    for i in range(len(s)):
        first_char = s[i]
        remaining_chars = s[:i] + s[i+1:]
        for p in permute(remaining_chars):
            res.append(first_char + p)
    return res

s = input().strip()
permutations = permute(s)
for p in sorted(permutations):
    print(p)