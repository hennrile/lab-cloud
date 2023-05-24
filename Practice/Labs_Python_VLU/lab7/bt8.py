'''Viết chương trình kiểm tra số nguyên tố
Số nguyên tố là số chỉ chia hết cho 1 và chính nó
VD: 2,3,5,7,11 là số nguyên tố'''

import math 
n = int(input("Enter a number: "))
flag = False

#for i inrange(2,n+1,1)
for i in range (2, int(math.sqrt(n)+1)):
    if n % i == 0:
        flag = True
        break
if flag == True:
    print("The number isn't a prime")
else:
    print("The number is a prime")