# Mad Libs Story Generator
# This program prompts the user for various words and constructs a humorous story.
# It includes default values for inputs.


print("Please enter the following information")
print("")

def safe_input(prompt: str, default: str = "") -> str:
	"""Trim input and use default if empty."""
	try:
		val = input(prompt).strip()
	except EOFError:
		# Allow non-interactive runs to proceed with default
		val = ""
	return val if val else default

adjective = safe_input("adjective: ", "mysterious")
animal = safe_input("animal: ", "raccoon")
verb1 = safe_input("verb (past tense): ", "scurried")
exclamation = safe_input("exclamation: ", "wow")
verb2 = safe_input("verb (present): ", "dance")
verb3 = safe_input("verb (infinitive): ", "sing")

print("")
print("Your story is")
print("")
print(f'The other day, I was really in trouble. It all started when I saw a very {adjective} {animal} {verb1} down the hallway. \"{exclamation.capitalize()}!\" I yelled. But all I could think to do was to {verb2} over and over. Miraculously, that caused it to stop, but not before it tried to {verb3} right in front of my family.')
