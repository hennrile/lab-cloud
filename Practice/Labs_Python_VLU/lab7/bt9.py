so_1 = 0
so_2 = 1
so_3 = ''
n = int(input("Enter number of fibonacci: "))
i = 0

for i in range(1,n+1):
	if (i <= 1):
		print(so_2)
	else:
		so_3 = so_1 + so_2
		so_1 = so_2
		so_2 = so_3
		print(so_3)