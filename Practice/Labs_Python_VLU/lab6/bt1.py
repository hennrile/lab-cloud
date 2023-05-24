a = int(input("Nhap 1 so nguyen duong <1000 : "))
total = 0
b = 0

if 0 < a < 1000:
    while a > 0:
        b = a % 10
        total += b
        a = a / 10
    print(f"tong cac phan tu cua so ban nhap la: {int(total)} ")
else:
    print("ban da nhap sai vui long nhap lai")