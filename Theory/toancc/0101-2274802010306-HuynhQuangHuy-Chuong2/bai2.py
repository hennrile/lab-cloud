def dem_soluong(n):
    if n == 0:
        return 0 
    else:
         return 1 + dem_soluong(n/10)
n=int(input('Nhập vào số nguyên n:'))
print(dem_soluong(n))