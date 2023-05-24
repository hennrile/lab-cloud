def triangle(a,b,c):
    if a + b >= c or a + c >= b or b + c >= a:
        if a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or b**2 + c**2 == a**2:
            return("Tam Giac Vuong")
        elif a == c and c == b:
            return("Tam Giac Deu")
        elif a == b or a == c:
            return("Tam Giac Can")
        else:
            return("Tam Giac Nhon")
    else:
        return("Khong phai la tam giac")

a = float(input("Nhap canh a: "))
b = float(input("Nhap canh b: "))
c = float(input("Nhap canh c: "))
    
#triangle(a, b, c)
print(triangle(a, b, c))
