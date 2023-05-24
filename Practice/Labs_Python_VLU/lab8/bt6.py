a = str(input("Enter a string: "))
lst = []
count = 0

b = a.split(' ')

for i in b:
    count += 1

print(count)