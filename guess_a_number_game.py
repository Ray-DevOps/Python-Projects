# This is the code for a guessing game whereby the system randomly chooses a secret number
# between 1 and 100, and asks the player to guess the number.
# First, the player is asked to chose a difficulty level "easy" or "hard".
# If the user choses "easy", they get 10 attempts to make the correct guess, and the game informs them of that.
# If the user choses "hard", they get only 5 attempts to make the correct guess, and the game informs them of that.
# Anytime the user makes an attempts and misses, the game prompts them to try again and also announces 
# how many more attempts they have left. If they run out of attempts, they loose and the game ends.
# If they guess the right number before running out of attempts, they win and the game ends


import random
numbers = list(range(1, 101))
secret_number = random.choice(numbers)
max_attempts = 1
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty_level = (input("Choose a difficulty. Type 'easy' or 'hard': ")).lower()

if difficulty_level == "easy":
    max_attempts = 10
    print("You'll get 10 attempts to guess the secret number")
elif difficulty_level == "hard":
    max_attempts = 5
    print("You'll get 5 attempts to guess the secret number")
else:
    print("You can only enter either 'easy' or 'hard'. Please start all over")

def guess_game():
    attempt_count = 0
    while attempt_count <= max_attempts and (difficulty_level == "easy" or difficulty_level == "hard"):
        attempt_count = attempt_count + 1
        guess = int(input("Please guess a number between 1 and 100: "))
        remainder_attempts = max_attempts - attempt_count
        if guess == secret_number:
            print("You got it right. You have won!")
            break
        elif guess > secret_number and attempt_count < max_attempts and remainder_attempts != 1:
            print(f"Your guess is higher than the secret number. You have {remainder_attempts} attempts left")
        elif guess < secret_number and attempt_count < max_attempts and remainder_attempts != 1:
            print(f"Your guess is lower than the secret number. You have {remainder_attempts} attempts left")
        elif guess > secret_number and remainder_attempts == 1:
            print(f"Your guess is higher than the secret number. You have one final attempt left")
        elif guess < secret_number and remainder_attempts == 1:
            print(f"Your guess is lower than the secret number. You have one final attempt left")
        else:
            print("Sorry! You have exhausted all your chances. Game over!")
            break

guess_game()
