mystring = "0983876207;75;10:18:25;0918295063"

arr1 = mystring.split(';')

time1 = int(arr1[1])

money_number_1 = (2500 * time1)

print(f"the phone number {arr1[0]} has call in {time1}m, the money has pay is {money_number_1}d")
