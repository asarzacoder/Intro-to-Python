# Mini Project: Number Guessing Game (with stats)

"""
Description: CLI game where computer picks a secret number, the user keeps guessing until they get it,
while tracking stats.

Requirements:
    + Secret number
    + Loops for guessing until correct
    + Feedbacks for user inputs:
        - Guessing too low
        - Guessing too high
    + Tacking attempts
    + Input validation
        - Must be between (1 - 100)
Additional(s):
    + Limited attempts
    + Track best attempt / score
"""

import random   # import for random generating number

print("Welcome to the Number Guessing Game!")

re_play = "y"
while re_play == "y":
    print("Generating secret number...")
    print("Complete!")
    secret_num = random.randint(1, 100) # picks a random number for guessing

    score = 0
    for guess in range (7, 0, -1):

        # Get user guess
        user_guesses = int(input(f"You have {guess} guesses left: "))

        # Validate guess is between 1 - 100
        while user_guesses < 1 or user_guesses > 100:
            print("Invalid input!")
            user_guesses = int(input(f"You have {guess} guesses left: "))

        score += 1
        if user_guesses == secret_num:
            print("CONGRATULATIONS! YOU GOT IT!")
            print("The secret number was: " + str(secret_num))
            print("Attempts used:", score)
            break
        else:
            if user_guesses < secret_num:
                print("Too low!")
            else:
                print("Too high!")

            if guess == 1:  # Show secret number upon running out of guesses
                print("You have ran out of guesses!")
                print("The secret number was: " + str(secret_num))
                print("YOU LOSE!")
                break

    print("Would you like to play again? (y/n)")
    re_play = input()

