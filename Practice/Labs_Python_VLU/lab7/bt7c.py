import array
n = ''
a = []
count = 0

while True:
    n = int(input("Enter number: "))
    if n <= 0:
        print("Incorrect! Please try again")
        continue
    break

for i in range (1, n + 1):
    if (n % i == 0): 
        a.append(i)

for x in a:
    count += 1

if count == 2:
    print(f"{n} is a prime numbers")
else:
    print(f"{n} isn't a prime numbers")