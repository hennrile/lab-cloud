n = ''
lst = []
answer = []

while True:
    n = int(input("Enter total of number in list: "))
    try:
        if n <= 0:
            print("Incorrect! please try again (n >= 0)")
            continue
        break
    except:
        print("Vaild is wrong, please input a integer")

for i in range(1, n + 1):
    i = int(input(f"Enter integer number in list {i}: "))
    lst.append(i)

for v in lst:
    if (v % 2 != 0):
        answer.append(v)

print(answer)