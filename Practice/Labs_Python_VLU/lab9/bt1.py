sum = 0
b = []

a = int(input("Enter size of list: "))

for i in range (1, a + 1):
	i = int(input(f"Enter the value number {i} of list: "))
	b.append(i)

print(b)

for x in b:
	sum += x

print(sum)