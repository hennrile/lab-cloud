'''
Nhập vào 1 số nguyên dương n,
Đếm xem n có bao nhiêu chữ số, tìm ra chữ số lớn nhất, và chữ số nhỏ nhất
vd:
n = 216935
* Có 6 chữ số 
* Chữ số Min = 1, Chữ số Max = 9
'''

n = int(input("Enter number: "))
count = 0
smallest = 9
largest = 0

while n > 0:
    digit = n % 10
    count += 1 
    if digit > largest:
        largest = digit
    if digit < smallest:
        smallest = digit
    n = n // 10 
print(f"The total of digits: {count}")
print(f"The number smallest: {smallest}")
print(f"The number largest: {largest}")