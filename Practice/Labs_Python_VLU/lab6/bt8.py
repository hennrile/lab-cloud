from random import *

a = randint(1, 6)

while True:
    b = int(input("Doan so a trong doan tu 1 toi 5: "))
    if a == b:
        print("ban da doan dung")
        break
    else:
        continue