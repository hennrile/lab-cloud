import math
a, b, c = [float(x) for x in input().split()]
x1 = 0
x2 = 0
s = 0

delta = b**2 - (4 * a * c)

while True:
    if delta > 0:
        x1 = round((-b - math.sqrt(delta)) / (2*a), 2)
        x2 = round((-b + math.sqrt(delta)) / (2*a), 2)
        if x1 < x2:
            print(x1, ", ", x2)
        else:
            print(x2, ", ", x1)
        break
    elif delta == 0:
        print((-b)/(2 * a))
        break
    else:
        print("NO")
        break