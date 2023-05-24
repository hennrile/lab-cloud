class Employee:
    def __init__(self, manv: str, ten_nv: str, ngay_sinh: str, luong: float):
        self.manv = manv
        self.ten_nv = ten_nv
        self.ngay_sinh = ngay_sinh
        self.luong = luong

    def hienthi_thongtin(self):
        print(f"Thông tin nhân viên:\nMã NV: {self.manv}\nTên NV: {self.ten_nv}\nNgày sinh: {self.ngay_sinh}\nLương: {self.luong}")
        
manv = input("Nhập mã nhân viên: ")
ten_nv = input("Nhập tên nhân viên: ")
ngay_sinh = input("Nhập ngày sinh (dd/mm/yyyy): ")
luong = float(input("Nhập lương: "))

nv = Employee(manv=manv, ten_nv=ten_nv, ngay_sinh=ngay_sinh, luong=luong)
nv.hienthi_thongtin()