row = ' ' #Khoi tao bien rong
while True: #Cho dk la true, lap toi khi nao nhap dung thi dung
    try: #xu ly doan code nghi ngo loi
        row = int(input("Enter a number: ")) #cho nhap vao 1 so nguyen
        if row < 0: #neu nhap sai (co nghia la nhap so am ) thi hien thi loi
            print("Sorry, enter in the format (row > 0)")
            continue #sau do bat dau 1 vong lap moi
        break # neu nhap dung thi se thoat khoi vong lap
    # neu nhap gia tri sai
    #thi doan code loi se hien thi o day
    except:
        print("Not vaild, Please enter a number again")
print(f"You enter: {row}") # hien thi ket qua vua nhap

# lap qua so dong
for i in range (0, row):
    # lap qua tu ky hieu *
    for j in range (0, i + 1):
        #moi lan in ki tu * va khong cho xuong dong
        print("* ",end="")
    print() #cho xuong dong