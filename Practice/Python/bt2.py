s1 = str(input("Enter string number one: "))
s2 = str(input("Enter string number two: "))

tmp = s1[0:2] + s2[2:]
s1 = s2[0:2] + s1[2:]
s2 = tmp

print(s1 +" "+ s2)
