import math
a=float(input("a: "))
b=float(input("b: "))
h=float(input("h: "))
n=int((b-a)/h+1e-9)+1
for i in range(n):
    x=a+i*h
    y=math.pow(2,x)/abs(x*x+1)+math.log2(abs(abs(x)+1))
    print("%i x=%.2f y=%.4f"%(i,x,y))


import math
a=float(input("a: "))
b=float(input("b: "))
h=float(input("h: "))
x=a
while x<=b+1e-9:
    y=math.pow(2,x)/abs(x*x+1)+math.log2(abs(abs(x)+1))
    print("x=%.2f y=%.4f"%(x,y))
    x=x+h


import math
a=float(input("a: "))
b=float(input("b: "))
h=float(input("h: "))
if h<=0 or a>b:
    print("потрібно h>0 і a<=b")
else:
    x=a
    spisok=[]
    while x<=b+1e-9:
        y=math.pow(2,x)/abs(x*x+1)+math.log2(abs(abs(x)+1))
        spisok.append(y)
        x=x+h
    for znach in spisok:
        print(znach)
    print("Найбільше:",max(spisok))
    print("Найменше:",min(spisok))