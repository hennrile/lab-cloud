def idn(n):
    if (n == 0):
        return 0 
    else:
        global nd 
        m = n % 10
        nd += str(m) # nd = nd + str(m)
        idn(n//10)
nd = ""
n = int(input("Nhập sô nguyên :"))
idn(n)
print(nd)
