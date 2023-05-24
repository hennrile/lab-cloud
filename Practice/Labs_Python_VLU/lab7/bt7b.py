import math

n = ''

while True:
    n = int(input("Enter number: "))
    if n <= 0:
        print("Incorrect! Please try again (n >0)")
        continue
    break

if math.sqrt(n) % 1 == 0:
    print("it's square number")
else:
    print("it's not square number")
