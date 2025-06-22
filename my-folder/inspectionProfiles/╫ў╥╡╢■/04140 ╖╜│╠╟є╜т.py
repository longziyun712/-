'''
def f(x):
    return x**3-5*x**2+10*x-80
x=5 #f(5)>0
x1=6 #f(6)<0


while abs(x - x1) >1e-14:   abs判断绝对值！！！！！！
    mid = (x + x1) / 2  #mid要放在循环里面
    if f(x) * f(mid) < 0:
        x1 = mid
    else:
        x =mid
print('{:.9f}'.format(x)) 或者 print('%.9f' % x)
'''
def f(x):
    return x ** 3 - 5 * x ** 2 + 10 * x - 80
def ff(x):
    return 3*x**2-10*x+10
x1=6
while True:
    x=x1-f(x1)/ff(x1)
    if abs(x-x1)<1e-12:
        break
    else:
        x1=x
print('%.9f'%x)