# Mad Libs Story Generator
# This program prompts the user for various words and constructs a humorous story.
# It includes enhancements such as additional prompts for a richer story,
# improved handling of articles ("a" vs "an"), and default values for inputs.

import random

def article(word: str) -> str:
	"""Return 'a' or 'an' for simple English heuristics."""
	w = (word or "").strip().lower()
	if not w:
		return "a"
	# words that begin with vowel sound exceptions (consonant letter but vowel sound)
	an_exceptions = ("honest", "hour", "honor", "heir")
	for ex in an_exceptions:
		if w.startswith(ex):
			return "an"
	# common 'u' and 'one' words that sound like a consonant (use "a")
	a_prefixes = ("uni", "univ", "use", "user", "euro", "one", "ouija")
	for p in a_prefixes:
		if w.startswith(p):
			return "a"
	# default: words that start with a vowel letter -> 'an'
	if w[0] in "aeiou":
		return "an"
	return "a"

def safe_input(prompt: str, default: str = "") -> str:
	"""Trim input and use default if empty."""
	try:
		val = input(prompt).strip()
	except EOFError:
		# Allow non-interactive runs to proceed with default
		val = ""
	return val if val else default

print("Please enter the following information")
print("")

# original prompts (kept) and several new ones
adjective = safe_input("adjective: ", "mysterious")
animal = safe_input("animal: ", "raccoon")
verb1 = safe_input("verb (past tense): ", "scurried")
exclamation = safe_input("exclamation: ", "wow")
verb2 = safe_input("verb (present): ", "dance")
verb3 = safe_input("verb (infinitive): ", "sing")

# new prompts to make story richer
name = safe_input("a name (person): ", "alex")
place = safe_input("place: ", "park")
profession = safe_input("profession: ", "magician")
clothing = safe_input("article of clothing: ", "hat")
number = safe_input("a number: ", "3")
color = safe_input("color: ", "blue")
food = safe_input("favorite food: ", "pizza")
noun = safe_input("noun: ", "bicycle")
plural_noun = safe_input("plural noun: ", "shoes")
emotion = safe_input("emotion: ", "surprised")
sound = safe_input("sound (onomatopoeia): ", "thump")

# polish some inputs
exclamation_word = exclamation.strip()
if not exclamation_word:
	exclamation_word = "wow"
# pick a small variation
exclamations = [exclamation_word.capitalize(), exclamation_word.upper() + "!", f"My {exclamation_word}!"]
chosen_excl = random.choice(exclamations)

print("")
print("Your story is")
print("")

# Build story using article helper and variables
print(f"The other day, I was really in trouble. It all started when I saw {article(adjective)} very {adjective} {animal} {verb1} down the hallway.")
print(f"\"{chosen_excl}\" I yelled. But all I could think to do was {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family.")
print("")
print(f"Later, {name.capitalize()} — who works as {article(profession)} {profession} in the {place} — showed up wearing {article(clothing)} {clothing}.")
print(f"They said they had seen {number} {color} {plural_noun} and were carrying {article(food)} {food} in a small {noun}.")
print("")
print(f"It was one of those days where everyone felt {emotion}. You could hear a distant {sound} every few minutes, which made the story even stranger.")
print("")
print("When the story finally ended, we all laughed and promised to never forget the day the")
print(f"{animal} decided to {verb3} during dinner. It turns out that sometimes all you need is {article(noun)} {noun} and a little imagination.")
print("")
