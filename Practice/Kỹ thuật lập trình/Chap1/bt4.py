def nhapds(n):
    ds = []
    for i in range (n):
        print(f"ds{i}: ",end="")
        a = int(input())
        ds.append(a)
    return ds

def tontai(x, ds):
    if x in ds:
        return True
    else:
        return False

n = int(input("nhap vao so phan tu trong danh sach: "))
ds = nhapds(n) 

x = int(input("Nhap gia tri x: "))
print(tontai(x, ds))