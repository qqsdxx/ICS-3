names = ("Водень", "Гелій", "Літій", "Берилій", "Бор",
         "Вуглець", "Азот", "Кисень", "Фтор", "Неон")

elements = dict()
for name in names:
    elements[name] = input("Введіть позначення елемента " + name + ": ")

print("\n Словник в алфавітному порядку:")
for key in sorted(elements):
    print(key, "-", elements[key])