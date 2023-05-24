print("Check your input string has in 'Viet Nam dat nuoc toi yeu' ?")

s1 = "Viet Nam dat nuoc toi yeu"
s2 = str(input("Enter your string: "))

if s2 in s1:
    print(f"string '{s2}' in string '{s1}'")
else: 
    print(f"string '{s2}' not in string '{s1}'")