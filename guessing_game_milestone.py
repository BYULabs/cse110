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
while True:
    guess = input("What is your guess? ").lower()
    guess_count += 1   

    if guess.lower() == word.lower():
        print("Congratulations! You guessed it!")
        print(f"It took you {guess_count} guesses.")
        break
    else:
        print("Your guess was not correct.")
