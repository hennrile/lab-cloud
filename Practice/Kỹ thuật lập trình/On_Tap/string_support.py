#bai tap 10
def dao_nguoc_chuoi(x):
    li = []
    for y in x:
        li.append(y)
    new_li = li[::-1]
    return new_li
    
#bai tap 11
def blank_space(x):
    li = x.replace(" ", "")
    return li
#bai tap 14
import string
def password(x):
    chu_hoa = chu_thuong = so = 0
    li = []
    for a in x:
        li.append(a)
    for y in li:
        if y in string.ascii_lowercase:
            chu_thuong += 1
        elif y in string.ascii_uppercase:
            chu_hoa += 1
        elif y in string.digits:
            so += 1
    if chu_hoa > 0 and chu_thuong > 0 and so > 0:
        return("Password hop le")
    else:
        return("Password khong hop le")
#bai tap 15
def vi_tri(x, y):
    cout = 0
    li = []
    for a in x:
        cout += 1
        if y == a:
            return(f"tu {y} nam o vi tri {cout} trong chuoi")
        elif y != a:
            continue
