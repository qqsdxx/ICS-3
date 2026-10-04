import math
x=float(input("x: "))
if x>=5.1:
    y=math.log2(3*x)-7*math.sqrt(x)
elif x>-0.7:
    y=math.exp(x)+2*x**3
else:
    y=math.exp(x)+math.sin(x+math.pi/4)
print("f(x)=",y)

a=float(input("Сторона a: "))
x=float(input("Координата x: "))
y=float(input("Координата y: "))
if a<=0:
    print("a Повинна бути додатною")
elif abs(x)<=a/2 and abs(y)<=a/2:
    print("Точка належить квадрату")
else:
    print("Точка не належить квадрату")