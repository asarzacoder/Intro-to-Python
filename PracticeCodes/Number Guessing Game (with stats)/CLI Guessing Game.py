# Mini Project: Number Guessing Game (with stats)

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

