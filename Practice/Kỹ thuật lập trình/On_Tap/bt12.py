li = [1,2,3,4,5,6,7,8]
li2 = [2,10,11,23,34]

x = int(input("Nhap so ban can tim: "))

if x in li and x in li2:
    print("so ban nhap ton tai trong hai danh sach")
elif x in li and x not in li2  or x not in li and x in li2:
    print("So ban nhap chi ton tai trong mot danh sach")
else:
    print("So ban nhap khong ton tai trong ca hai danh sach")