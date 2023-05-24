'''Trò chơi Tài Xỉu
Cách chơi: nếu đổ 3 dice >= 11 thì nó sẽ là Tài, ngược lại là xỉu
Hiển thị: 
Chọn Tài hay Xỉu, và mức cược
Nếu bạn thắng, thì sẽ được cộng tiền, và ngược lại'''
import random

bet = 0 
global result

def dice():
    return random.randint(1, 6)

def main():
    cash = 100

    while cash > 0:
        dice1 = dice()
        dice2 = dice()
        dice3 = dice()
        total = dice1 + dice2 + dice3
        if total >= 11:
            result = "tai"
        else:
            result = "xiu"
        
        user_input = input("\nBan chon tai hay xiu, neu muon thoat hay bam q : ").lower()
        if user_input == "q":
            quit()

        while True:
            bet = int(input(f"Nhap so tien ban cuoc, ban co {cash}$: "))
            if bet <= cash:
                break
            else:
                print("\nBan khong du tien, vui long thu lai")
                continue

        if user_input == result:
            print(total, result)
            cash = cash + bet
            print(f"Ban da thang {bet}$, so tien con lai cua ban la {cash}$")
        else:
            print(total, result)
            cash = cash - bet
            print(f"Ban da thua {bet}$, so tien con lai cua ban la {cash}$")
            print("\n nga o dau gap doi o do chu ha :D")

    print("Ban da thua het tien, vui long nap them")
    quit()

print('''\tNoHu.com
Tro choi Tai Xiu, tien ban dang co la 100$''')

while True:
    print(main())