def tinhtong(n):
    if n==0:
        tong= 1
    else:
        tong= tinhtong(n-1)*(n*2+1)
n=int(input('Nhập vào số nguyên n:'))
print(tinhtong(n))