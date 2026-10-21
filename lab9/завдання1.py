A = ("one", "two", "three", "four", "five",
     "six", "seven", "eight", "nine", "ten")

digits = input("Введіть числа від 1 до 10 через пробіл: ").split()
B = tuple(A[int(d) - 1] for d in digits)

print("Кортеж B:", B)