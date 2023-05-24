a = []
max = 0
total = 0

for i in range (1,6):
    i = float(input(f"Nhap phan tu con cua list thu tu so {i}: "))
    a.append(i)

for x in a:
    if x > max:
        max = x

for y in a: 
    total += y

print(a)
print(f"So lon nhat trong list la: {max}")
print(f"Tong cac phan tu la: {total}")