i = int(input("Nhap i: "))
total = 0

for n in range (0, i + 1):
    if n == 17:
        continue
    total += n
print(f"result {total}")