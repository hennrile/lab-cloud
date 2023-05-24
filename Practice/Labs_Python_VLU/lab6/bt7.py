a = int(input("Nhap a: "))
sum = 0 

for i in range (0, a + 1):
	if i < 13:
		sum += i
	elif i == 13:
		break
print(f"tong la: {sum}")