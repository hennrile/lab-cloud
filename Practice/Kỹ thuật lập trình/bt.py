def add_average(number):
    index = 0 
    total = 0
    while True:
        if index == len(number):
            return total / len(number)
        else:
            index += 1
            total += number[index - 1]
            continue
num_of_number = int(input("Do dai chuoi (Lenght of str): "))
number = []
for i in range(1, num_of_number + 1):
    i = int(input("Nhap gia tri (Value): "))
    number.append(i)

print(add_average(number))