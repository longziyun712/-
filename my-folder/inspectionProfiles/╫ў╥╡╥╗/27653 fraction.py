def gcd(x,y): #最大公约数
    while y:
        x,y=y,x%y
    return x
class Fraction:
    def __init__(self,num,den):
        if den == 0:
            raise ValueError("分母不能为0")
        gys=gcd(abs(num),abs(den))
        self.n=num//gys
        self.d=den//gys

    def __add__(self,other):
        add_n=self.n*other.d+self.d*other.n
        add_d=self.d*other.d
        return Fraction(add_n,add_d)

    def __str__(self,):
        return(f'{self.n}/{self.d}')

a,b,c,d=[int(x) for x in input().split()]

f1 = Fraction(a,b)
f2 = Fraction(c,d)
print(f1+f2)
