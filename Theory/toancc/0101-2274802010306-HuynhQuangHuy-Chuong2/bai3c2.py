def indn(n):
    if n<10:
        return str(n)
    else:
        return str(n%10)+indn(n//10)
n=int(input("Nhập số để đảo ngược:"))
print(indn(n))
