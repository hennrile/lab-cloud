a = int(input("Nhap tong so trong mang: "))
b = []
sum = 0

for i in range (0, a):
	i = int(input("Nhap gia tri mang "))
	sum += i
	b.append(i)

print (f"trung binh cong cua mang co {a} gia tri la {sum / a}")