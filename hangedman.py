import random


print("Welcome to the Hanged Man game!")

WORDS = [
  "Python",
  "Challenge",
  "Hangman",
  "Developer",
  "Algorithm",
  "Function",
  "Variable",
  "Interface",
  "Repository",
]

word = random.choice(WORDS)
max_attempts = 6
guessed_letters = set()
attempts_left = max_attempts

print(f"You have {max_attempts} attempts to guess the word. Enter one letter per guess.")

def display_progress(target_word, guessed):
    shown = []
    for ch in target_word:
        if not ch.isalpha() or ch.lower() in guessed:
            shown.append(ch)
        else:
            shown.append("_")
    return " ".join(shown)

def all_guessed(target_word, guessed):
    return all((not c.isalpha()) or (c.lower() in guessed) for c in target_word)

while attempts_left > 0 and not all_guessed(word, guessed_letters):
    print()
    print("Word:", display_progress(word, guessed_letters))
    print("Guessed letters:", ", ".join(sorted(guessed_letters)) if guessed_letters else "(none)")
    print(f"Attempts left: {attempts_left}")

    guess = input("Guess a letter (or type the full word): ").strip()
    if not guess:
        print("Please enter a letter or a word.")
        continue

    # If user tries to guess the whole word
    if len(guess) > 1:
        if guess.lower() == word.lower():
            guessed_letters.update({c.lower() for c in word if c.isalpha()})
            break
        else:
            attempts_left -= 1
            print("Wrong guess for the whole word.")
            continue

    # single-letter guess
    if not guess.isalpha():
        print("Please enter a valid alphabetic character.")
        continue

    g = guess.lower()
    if g in guessed_letters:
        print("You've already guessed that letter.")
        continue

    guessed_letters.add(g)
    if g in word.lower():
        print("Good guess!")
    else:
        attempts_left -= 1
        print("Nope, that letter is not in the word.")

print()
if all_guessed(word, guessed_letters):
    print("Congratulations! You guessed the word:", word)
else:
    print("Out of attempts. The word was:", word)
