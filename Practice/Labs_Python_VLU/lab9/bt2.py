product = 1 
a = []
tich = 1

n = int(input("Enter size of list: "))

for i in range (1, n+1):
    i = int(input())
    a.append(i)

for x in a:
    tich *= x

print(tich)