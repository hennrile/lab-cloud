lst = []
max = 0

a = int(input("Size of the list: "))

for i in range (1, a + 1):
    i = int(input("Value of list: "))
    lst.append(i)
lst.sort()
print(lst[-1])

for x in lst:
    if x >= max:
        max = x
        continue

print(max)