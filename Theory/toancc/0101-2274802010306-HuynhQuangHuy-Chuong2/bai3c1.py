def InNguoc(n):
    if n ==0:
        return ""
    else:
        m=n%10
        print(m,end="")
        return InNguoc(n//10)
    
n=int(input("Nhập số để đảo ngược: "))
print(InNguoc(n))
