import numpy as np

row1 = input("введіть перший рядок чисел через пробіл: ").split()
row2 = input("введіть другий рядок чисел через пробіл:").split()

if len(row1) != len(row2):
    print("рядки повинні містити однакову кількість чисел!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
else: 
    n = len(row1)
    M = np.zeros((2, n), dtype=int)

    for j in range(n):
        M[0][j] = int(row1[j])
        M[1][j] = int(row2[j])

    P = np.zeros(n, dtype=int)
    for j in range(n):
        for i in range(2):
            P[j] += M[i][j]

    print("Масив M: ")
    print(M)
    print("Мавсив P (суми по стовпчиках):")
    print(P)