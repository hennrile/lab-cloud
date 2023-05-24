def songuyento(a):
    if a <= 1:
        return True
    for i in range (2,a):
        if a % i == 0:
            return True
    return False        
a = int(input("Nhap de: "))                    
print(songuyento(a))
if songuyento(a) == False:
    print("la so nguyen to")
else:
    print("khong phai so nguyen to")    