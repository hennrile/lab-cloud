'''
Nhập một số nguyên dương n (n > 0). Hãy cho biết:
a. Có phải là số đối xứng ? VD: 121, 12021
Số nguyên gọi là đối xứng nếu đọc từ trái qua phải hay từ phải qua trái đều được số giống nhau
vd: 11, 121, 12321, đó là số đối xứng
Ý tưởng: 
b1: Tìm số đảo
b2: So sánh số đảo đó và số nguyên nhập vào
b3: Kiểm tra nêu bằng nhau rhif là số đảo, và ngược lại
'''

n = int(input("Enter a number: ")) 
temp = n 
rev = 0 
while n > 0:
    digit = n % 10 #Lấy chữ số cuối cùng dùng toán tử modulus (%)
    rev = ( rev * 10 ) + digit #Nhân số đảo với 10 + chữ số vừa tách
    n = n // 10 #xoá chữ số cuối cùng

if rev == temp:
    print("The number is a palindrome")
else: 
    print("The number isn't a palindrome")