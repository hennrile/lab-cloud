def daonguocso(x):
    if x < 10:
        return x
    else: 
        return (x % 10) * (10 ** (len(str(x)) - 1)) + daonguocso(x // 10)

x = int(input("Nhap so ban muon dao nguoc: "))
print(daonguocso(x))
