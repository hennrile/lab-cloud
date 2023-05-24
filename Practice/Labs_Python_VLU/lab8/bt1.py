a = str(input("Enter your name: "))
b = str(input("Enter your name of university: "))

c = len(a.replace(" ", ""))
d = len(b.replace(" ", ""))

print(f"Your name has {c} characters")
print(f"Your university has {d} characters")
print(f"total characters of your name and university is {c + d}")

z = b + " " + a

print(f"Your input {z}")