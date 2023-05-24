''': Love Calculator
Instructions
You are going to write a program that tests the compatibility between two people.
To work out the love score between two people:
Take both people's names and check for the number of times the letters in the word TRUE
occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number'''
print("Bai Tap 8:a")
print("Welcome to python love calculator program")

p1 = input("What is the name of person 1 : ")
p2 = input("What is the name of person 2: ")

len1 = (len(p1))
len2 = (len(p2))

len_p = 20 if len1 == len2 else 5
first_char = 50 if p1[0] == p2[0] else 5
last_char = 30 if p1[len1 - 1] == p2[len2 - 1] else 5

percentage =  len_p + first_char + last_char

print(f"Your love is {percentage}% true")