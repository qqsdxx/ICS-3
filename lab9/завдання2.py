T = set(range(102, 251, 3))   
S = set(range(102, 251, 6))  

print("Початкова множина T:", sorted(T))
T = T - S                     
print("Множина T після видалення кратних 6:", sorted(T))