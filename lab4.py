import math

x = float(input("x: "))

крутафункшн = ((x - 4)**3 + math.log(x)) / abs(x + 1 / math.tan(x)) + math.cos(x + 2)**3
print("крута функшн(x) =", крутафункшн)

x = float(input("x: "))
y = float(input("y: "))
z = float(input("z: "))

R = 12 * (x**2 + math.sin(y)) + math.sqrt(z**2 + 1) / (math.log(abs(z), 3) + 0.07)
print("R =", R)