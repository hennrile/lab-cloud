from typing import Any
import os

class Hoc_Sinh:
    global grade 
    grade = []
    def __init__(self, mssv = "", Ten = "", Toan = 0.0, Van = 0.0, Anh = 0.0):
        self.mssv = mssv
        self.Ten = Ten
        self.Toan = Toan
        self.Van = Van
        self.Anh = Anh
    
    def Nhap_Thong_Tin(self):
        self.mssv = input("Nhap mssv cua ban: ")
        self.Ten = input("Nhap Ten: ")
        self.Toan = float(input("Nhap diem Toan: "))
        grade.append(self.Toan)
        self.Van = float(input("Nhap diem Van: "))
        grade.append(self.Van)
        self.Anh = float(input("Nhap diem Anh: "))
        grade.append(self.Anh)


    def Show_info(self):
        print(f"MSSV: {self.mssv}")
        print(f"Ten: {self.Ten}")
        print(f"Diem Toan: {self.Toan}")
        print(f"Diem Van: {self.Van}")
        print(f"Diem Anh: {self.Anh}")

    def Diem_Trung_Binh(self):
        if (self.Toan + self.Van + self.Anh) / 3 >= 5:
            print(f"Diem cua ban la: {(self.Toan + self.Van + self.Anh) / 3}")
            print("Da dau")
        else:
            print(f"Diem cua ban la: {(self.Toan + self.Van + self.Anh) / 3}")
            print("Rot")

    def High_Low_Grade(self):
        max = 0.0
        min = 10.0
        for i in grade:
            if i > max:
                max = i
            if i <= min:
                min = i
        print(f"Max grade: {max}")
        print(f"Min grade: {min}")

sinh_vien = Hoc_Sinh()

while True:
    for i in grade:
        # print(i)
        with open("test.txt", "a+") as f:
            f.write("\n")
            f.write(str(i))

    # os.system("clear")
    def show():
        print('''\n Welcome
        1. Nhap Thong Tin
        2. Hien Thi Thong Tin
        3. Diem Trung Binh
        4. Diem cao nhat va thap nhat
        5. Thoat''')
        
        x = int(input("Choose(number): "))

        if x == 1:
            sinh_vien.Nhap_Thong_Tin()
        elif x == 2:
            sinh_vien.Show_info()
        elif x == 3:
            sinh_vien.Diem_Trung_Binh()
        elif x == 4:
            sinh_vien.High_Low_Grade()
        elif x == 5:
            quit()
    
    show()

