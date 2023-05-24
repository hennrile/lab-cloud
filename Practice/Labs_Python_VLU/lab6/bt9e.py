n = int(input("Nhap so n: "))

tich = 1
i = 1
tong = 0 

while i <= n: 
    tich = tich * i
    tong = tong + tich
    i += 1
print(tong  )