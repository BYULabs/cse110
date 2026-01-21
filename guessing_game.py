# This is a simple word guessing game where the player has to guess a randomly selected word from a predefined list.
# A function has been added to use instead of duplicating the code to generate the hint

import random
print("Welcome to the word guessing game!")
WORDS = [
    "Moroni",
    "Nephi",
    "Alma",
    "Mosiah",
    "Helaman",
    "Ether",
    "Lehi",
    "Laman",
    "Sam",
    "Zoram"
]
word = random.choice(WORDS)
guess = ""
guess_count = 0

def generate_hint(secret, player_guess):
    hint = ""
    for i in range(len(secret)):
        if i < len(player_guess) and player_guess[i].lower() == secret[i].lower():
            hint += secret[i].upper() + " "
        elif i < len(player_guess) and player_guess[i].lower() in secret.lower():
            hint += player_guess[i].lower() + " "
        else:
            hint += "_ "
    return hint

print(f"\nYour hint is: {generate_hint(word, guess)}")

while True:
    guess = input("What is your guess? ").lower()
    guess_count += 1   

    if len(guess) != len(word):
        print("Sorry, the guess must have the same number of letters as the secret word.")
        print()
    else:
        print(f"\nYour hint is: {generate_hint(word, guess)}")

    if guess.lower() == word.lower():
        print("Congratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")
        break