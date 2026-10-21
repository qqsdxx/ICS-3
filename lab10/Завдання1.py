alphabet = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

f = open("start.txt", "rt", encoding="utf-8")
text = f.read().lower()
f.close()

freq = dict()
for letter in alphabet:
    freq[letter] = text.count(letter)

f = open("fin.txt", "wt", encoding="utf-8")
for letter in alphabet:
    f.write(letter + ": " + str(freq[letter]) + "\n")
f.close()

print("Результат записано у файл fin.txt")