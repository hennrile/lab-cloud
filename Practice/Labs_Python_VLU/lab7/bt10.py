a = [500000, 200000, 100000, 50000, 20000, 10000, 5000, 2000, 1000, 500]
i = 0
so_tien_mon_do = ''
so_tien_ban_dua = ''
count = 0


while True:
    so_tien_mon_do = int(input("Nhap so tien ban can phai tra: "))
    so_tien_ban_dua = int(input("Nhap so tien ban dua: "))
    tien_thua = so_tien_ban_dua - so_tien_mon_do
    if tien_thua < 0:
        print("Ban da dua thieu tien")
        continue
    break

while tien_thua != 0:
    if (tien_thua >= a[i]):
        count = tien_thua / a[i]
        tien_thua %= a[i]

        print(f"To tien menh gia {a[i]} la: {int(count)}")
    i += 1 