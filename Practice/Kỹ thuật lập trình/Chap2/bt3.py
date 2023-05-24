def so_dao_nguoc(n):
    if n == 0:
        return
    else:
        m = n % 10
        print(m, end="")
        return so_dao_nguoc(n // 10)
n = int(input("Nhap 1 so: "))
a = 0
so_dao_nguoc(n)