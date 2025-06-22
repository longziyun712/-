while True:
    try:
        n=input()
    except EOFError:
        break
    m='YES'
    for i in range(len(n)):
        if n[i]!=n[len(n)-i-1]:
            m='NO'
            break
        else:
            continue
    print(m)
'''
import sys
for line in sys.stdin:
    n = line.strip()
    print("YES" if n == n[::-1] else "NO")'''