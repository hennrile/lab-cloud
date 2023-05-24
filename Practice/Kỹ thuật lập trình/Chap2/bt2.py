def dem_so (n):
    if n == 0:
        return 0
    else:
        m = n % 10
        global count 
        if m >= 0:
            count += 1
    dem_so(n // 10)
n = int(input("Nhap 1 so: "))
count = 0
dem_so(n)
print(count)