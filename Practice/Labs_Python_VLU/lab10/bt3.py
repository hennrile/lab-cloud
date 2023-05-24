# Nguyên liệu có sẵn
nguyen_lieu = ['cá', 'tôm', 'bò', 'heo', 'cua', 'bí đỏ', 'cà chua', 'hành tây', 'dưa leo', 'ớt', 'cà tím']

# Khởi tạo một giỏ hàng trống
giỏ_hàng = []

# Yêu cầu người dùng nhập số nguyên liệu mà họ muốn mua
so_luong_nguyen_lieu = int(input("Bạn muốn mua bao nhiêu nguyên liệu? "))

# Yêu cầu người dùng chọn nguyên liệu
for i in range(so_luong_nguyen_lieu):
    nguyen_lieu = input(f"Nhập nguyên liệu {i + 1}: ").lower()
    while nguyen_lieu not in nguyen_lieu:
        print(f"{nguyen_lieu} không có trong chợ.")
        nguyen_lieu = input(f"Nhập nguyên liệu {i + 1}: ").lower()
    if nguyen_lieu in giỏ_hàng:
        print(f"{nguyen_lieu} đã được thêm vào giỏ hàng.")
    else:
        giỏ_hàng.append(nguyen_lieu)

# Xóa các phần tử trùng lặp trong giỏ hàng
giỏ_hàng = list(set(giỏ_hàng))

# Hiển thị giỏ hàng cuối cùng
print("\nGiỏ hàng cuối cùng:")
for nguyen_lieu in giỏ_hàng:
    print(nguyen_lieu)