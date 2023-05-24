SBD = int(input("Nhap so bao danh: "))
Math = float(input("Nhap diem toan: "))
Language = float(input("Nhap diem ngoai ngu: "))
literature = float(input("Nhap diem van: "))
total = 0

print("-----")

print("\t--Phieu diem--")
print(f"\tSo bao danh: {SBD}")
print(f"\tDiem Van: {literature}")
print(f"\tDiem Toan: {Math}")
print(f"\tDiem Ngoai Ngu: {Language}")

print("-----")

total = Math + Language + literature

if total >= 15:
    print(f"Ban da trung tuyen voi so diem {total}")
else:
    print(f"Rat tiec ban con thieu {15 - total} diem de trung tuyen")