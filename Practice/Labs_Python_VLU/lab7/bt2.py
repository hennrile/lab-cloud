row = ''
col = ''

while True:
	try:
		row = int(input("Enter row:"))
		col = int(input("Enter column: "))
		if row <= 0 or col <= 0:
			print("Incorrect! Please try again")
			continue
		break
	except:
		print("wrong value, please number again")
print(f"The number of columns is {col}")
print(f"The number of rows is {row}")

for i in range (row):
	for j in range (col):
		print("* ",end = "")
	print()
