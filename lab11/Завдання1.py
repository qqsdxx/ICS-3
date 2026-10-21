import csv

filename = "ip.csv"

sites = dict()
fd = open(filename, "r", encoding="utf-8")
reader = csv.reader(fd, delimiter=":")
for row in reader:
    if len(row) == 2:
        sites[row[0].strip()] = row[1].strip()
fd.close()

print("Словник:", sites)

ip = input("Введіть IP-адресу: ").strip()
if ip in sites:
    print("Сайт:", sites[ip])
else:
    print("Таку IP-адресу не знайдено")