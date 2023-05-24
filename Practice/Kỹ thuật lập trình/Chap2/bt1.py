def so_lon_nhat(n):
    if n == 0:
        return
    else:
        m = n % 10 
        global max
        if m > max:
            max = m
    so_lon_nhat(n // 10)
n = int(input("Nhap vao so nguyen n: "))
max = 0 
so_lon_nhat(n)
print(max)