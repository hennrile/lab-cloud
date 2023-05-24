li = [1,2,3,4,5,6,7,8]
li2 = [2,10,11,23,34]

max = 0

for i in li:
    if i > max:
        max = i
    for i in li2:
        if i > max:
            max = i

print(max)