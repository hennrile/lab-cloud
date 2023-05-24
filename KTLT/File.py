from math import sqrt
with open('test.txt', 'r') as f:
    lines = f.readlines()
count = 0
for line in lines:
    numbers = line.strip().split()
    for number in numbers:
        if number.isdigit():
            if int(sqrt(int(number))) ** 2 == int(number):
                count += 1

print(f'Số lượng số chính phương trong file dulieu.txt là: {count}')