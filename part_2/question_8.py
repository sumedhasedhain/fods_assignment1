''' Program to run a number guessing game for the user
'''

import random

# Step I: Generate a random number between 1 and 100
answer = random.randint(1, 100)

# Step II: Initialize variables
max_attempts = 5
attempts = 0

# Step III: Start the game
print("Welcome to the Number Guessing Game!")
print(f"Try to guess the number between 1 and 100. You have {max_attempts} attempts.")

# Step IV: Loop through user guesses
while attempts < max_attempts:
    # Prompt the user to input a guess
    guess = int(input("Enter your guess: "))
    attempts += 1

    # Step III: Provide feedback after each guess
    if guess < answer:
        print("Too low!")
    elif guess > answer:
        print("Too high!")
    else:
        print("YAY Correct number! You've won!")
        break  # Exit the loop if the user guesses correctly

# Step V: Check if the user failed to guess in 5 attempts
if guess != answer:
    print("Game Over! You've used all your attempts.")
