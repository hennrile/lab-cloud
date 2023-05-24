import os

def kiemtra(x):
    if os.path.isfile(x) == True:
        a = open(x, "a+")
        content = input("Nhap noi dung ban muon them file: ")
        a.write("\n")
        a.write(content)
        print("file ban da ghi")
        a.seek(0)
        noi_dung = a.read()
        print("Noi dung file sau khi da ghi")
        print(noi_dung)
        a.close()
    else:
        print("file khong ton tai, se tao mot file moi")
        a = open(x, "a+")
        content = input("Nhap noi dung ban muon them file: ")
        a.write(content)
        a.seek(0)
        noi_dung = a.read()
        print("File sau khi ghi")
        print(noi_dung)
        a.close()
        
x = input("Nhap file hoac path file: ")
kiemtra(x)