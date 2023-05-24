lst2 = []

def sapxepgiamdan(w):
    for i in range(w):
        lst2.append(int(input(f"Nhap so {i}: ")))

    lst2.sort(reverse=True)

    print(lst2)

sapxepgiamdan(int(input("nhap so can tao list: ")))