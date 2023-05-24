import random 
import time

com = random.randint(1, 100)
cout = 0
starttime = time.time()

while cout < 7:
    player = int(input("Guessing a number 1 to 100: "))
    cout += 1
    if player == com:
        print("Chuc mung ban")
        break
    if player < com:
        print("So ban doan nho hon")
    elif player > com:
        print("So ban doan lon hon")