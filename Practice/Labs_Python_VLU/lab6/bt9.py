suma, sumb, sumc, vol = 0, 0, 0, 1
vol2, a, sumd = 1, 1, 0

n = int(input("mời bạn nhập số n:"))
for i in range(1, n + 1 ) :
    suma += 1
    sumb += i**2
    sumc += 1/i
    vol *= i
print(f"(1+2+3+4+...+n) là {suma}")
print(f"(1^2+2^2+3^2+...+n^2 là {sumb}")
print(f"(1+1/2+1/3+...+1/n) là {sumc}")
print(f"(1*2*3*...*n) là {vol}")