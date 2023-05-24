import random
import time

print("Let's play a number guessing game!")

# Generate a random number between 1 and 100
target = random.randint(1, 10)

# Keep track of number of attempts and start time
attempts = 0
start_time = time.time()

while attempts < 7:
    guess = int(input("Enter your guess (under 10): "))
    attempts += 1

    if guess == target:
        end_time = time.time()
        print("You won! Total attempts:", attempts)
        print("Total time taken:", end_time - start_time, "seconds")
        break
    elif guess < target:
        print("The target is higher.")
    else:
        print("The target is lower.")

if attempts == 7:
    print("You lost! The target was", target)
