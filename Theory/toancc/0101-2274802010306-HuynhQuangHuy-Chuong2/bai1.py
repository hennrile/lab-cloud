def sln(n):
    if n==0:
        return 0 
    else:
        m=n%10
        global max 
        if m>max:
         max=m
    sln(n//10)

n=int(input('Nhập vào số nguyên n:'))
max=0
print(sln(n))
print(max)