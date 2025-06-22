def Swap(x,y):
    tmp = x
    print(tmp, x, y)
    x = y
    print(tmp, x, y)
    y = tmp
    print(tmp,x,y)
a = 4
b = 5
Swap(a,b)
print(a,b)	#>>4, 5

def func(x):
    def g(y):
        #nonlocal x  #有了此行，才能在g中对x赋值
        x += 1
        return x+y
    return g
