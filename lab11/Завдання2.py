import json

with open("elements.json", "r", encoding="utf-8") as json_file:
    elements = json.load(json_file)

name = input("Введіть назву елемента: ").strip().capitalize()
if name in elements:
    print("Відносна атомна маса", name, "=", elements[name])
else:
    print("Такого елемента немає")

letter = input("Введіть літеру: ").strip().lower()
found = False
for key in elements:
    if key.lower().startswith(letter):
        print(key, "-", elements[key])
        found = True
if not found:
    print("Елементів на цю літеру немає")