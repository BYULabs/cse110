import random

keep_playing = "yes"

while keep_playing == "yes":
    secret_number = random.randint(1, 100)
    
    guess_count = 0

    while True:
        guess = int(input("What is your guess? "))
        guess_count += 1

        if guess == secret_number:
            print("Congratulations! You guessed the number.")
            break
        elif guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print("Sorry, you've run out of attempts. The number was:", secret_number)

    print(f"It took you {guess_count} attempts to guess the number.")

    keep_playing = input("Would you like to play again? (yes/no)")