import array

n = int(input("Enter numbers of child elenment: "))
a = []
x = 0

up = 0
down = 0 
flat = 0

for i in range (1, n + 1):
    i = int(input(f"Enter child element number {i}: "))
    a.append(i)

print(f"numbers: {a}")

for x in range (n):
    if x < (n - 1):
        if (a[x] == a[x + 1]):
            flat += 1
        elif (a[x] < a[x + 1]):
            up += 1
        elif (a[x] > a[x + 1]):
            down += 1
if (up == (n - 1)):
    print("element is increase")
elif (down == (n - 1)):
    print("element is decrease")
elif (flat == (n - 1)):
    print("element is flat")
else:
    print("element neither increase nor decrease")