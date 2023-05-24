dic = {
    2274802010306 : "Huynh Quang Huy",
    1703038 : "Pham Thi Minh Anh",
    2274802010123 : "Mr.A",
    2274802010234 : "Mss.B",        
}


print(dic)
while True:
    name = int(input("Nhap mssv nguoi ban can truy cuu: "))

    if name in dic.keys():
        print(dic.get(name).upper())
        break
    else:
        print("Khong co mssv vui long nhap lai")

cap_nhap = str(input("Ban co muon cap nhap thong tin khong (Y/N): "))
cap_nhap = cap_nhap.upper()
while cap_nhap == "Y":
    mssv = int(input("Nhap mssv ma ban can cap nhap thong tin: "))
    if mssv in dic.keys():
        print(f"Day la thong tin ma ban muon cap nhap: {dic.get(mssv)}")
        #Cách 1 để thay đổi thông tin trong dictionary
        dic [mssv] = str(input("Nhap thong tin can thay doi: "))
        #Cách 2 để thay đổi thông tin trong dictionary
        dic.update({mssv : str(input("Nhap thong tin can thay doi: "))})
        print(dic)
        break
    else:
        print("Ban nhap sai roi vui long nhap lai")
while cap_nhap == "N":
    print("Cam on ban")
    break
        