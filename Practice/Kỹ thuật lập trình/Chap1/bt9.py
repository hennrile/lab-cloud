def mua(thang):
    if thang in [1,2,3]:
        return "mua xuan"
    if thang in [4,5,6]:
        return "mua ha"
    if thang in [7,8,9]:
        return " mua thu"
    if thang in [10,11,12]:
        return "Mua dong"
    else:
        return "khong co thang nay"

thang = int (input("Nhap thang: "))

print(mua(thang))