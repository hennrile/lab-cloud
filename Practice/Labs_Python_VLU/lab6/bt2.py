a = int(input("Nhap a: "))
b = int(input("Nhap b: "))
c = int(input("Nhap c: "))

if (a + b > c) and (a + c > b) and (b + c > a) :
	print("3 so ban nhap la 1 canh tam giac")
	if (a**2 == b**2 + c**2) or (b**2 == a**2 + c**2) or (c**2 == b**2 + a**2):
		print("Day la 1 tam giac vuong")
	elif a == b == c:
		print("Day la tam giac deu")
	else:
		print("Day la tam giac nhon")

else:
	print("3 so ban nhap khong phai la 1 tam giac")