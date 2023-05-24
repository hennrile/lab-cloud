import random

player = str(input("Chon keo, bua, bao: "))

if player != "keo" and player != "bua" and player != "bao":
	print("Ban da nhap sai vui long nhap lai")
else:
	computer = random.randint(0, 2)

	if computer == 0:
		computer = "bua"
	if computer == 1:
		computer = "bao"
	if computer == 2:
		computer = "keo"

	print("-----")

	print(f"Ban chon {player}")
	print(f"May chon {computer}")

	print("------")

	if str(player) == str(computer) :
		print ("Hoa")

	else:

		if player == "keo":
			if computer == "bao":
				print("Ban da thang")
			else:
				print("Ban da thua")

		if player == "bua":
			if computer == "keo":
				print("Ban da thang")
			else:
				print("Ban da thua")

		if player == "bao":
			if computer == "bua":
				print("Ban da thang")
			else:
				print("Ban da thua")