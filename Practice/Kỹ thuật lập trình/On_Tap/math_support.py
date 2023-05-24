#bai tap 1
def add(x, y):
    b = x + y
    return b 
#bai tap 2
def so_trunng_gian(x, y, z):
    if (x > y > z) or (x < y < z):
        return(y)
    elif (y > x > z) or (y < x < z):
        return(x)
    elif (x > z > y) or (x < z < y):
        return(z)
#bai tap 3
def check_number(x):
    # Kiểm tra x có phải là số hay không
    if not isinstance(x, (int, float)):
        return False
    
    # Kiểm tra x là số thực hay số nguyên
    if isinstance(x, float):
        return True
    else:
        # Kiểm tra x là số nguyên âm, nguyên dương hay không
        if x < 0:
            return False
        elif x == 0:
            return True
        else:
            return True

#bai tap 4
def giai_he():
    
    print('''Giai he phuong trinh
    ax + by = c
    dx + ey = f
    tim x,y''')
    x = 0
    y = 0
    a = int(input("Nhap tham so a: "))
    b = int(input("Nhap tham so b: "))
    c = int(input("Nhap tham so c: "))
    d = int(input("Nhap tham so d: "))
    e = int(input("Nhap tham so e: "))
    f = int(input("Nhap tham so f: "))

    D = a*e - b*d
    Dx = c*e - f*b
    Dy = a*f - d*c

    if D != 0:
        x = Dx/D
        y = Dy/D
        return(f'''Pt co 2 nghiem 
        x = {x}
        y = {y}''') 
    elif D == 0:
        if Dx == Dy == 0:
            return("PT co vo so nghiem")
        elif Dx != 0 or Dy != 0:
            return("PT vo nghiem")

