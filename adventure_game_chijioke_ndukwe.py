print("You are walking through a dark forest and find two items: a MATCH and a FLASHLIGHT. Which one do you want to pick up?")

first_option = "flashlight"
second_option = "match"

choice = input("Enter an option: ")

if choice == first_option:
    print("You pick up the flashlight and turn it on. You see the pathway lit up in front of you, but you thought you also heard something off to the side.")
    while True:
        follow_choice = input("Do you want to FOLLOW the path or LOOK in the trees? (follow/look) ").strip().lower()
        if follow_choice in ("follow", "f"):
            print("You follow the path, staying alert for any movement in the trees.")
            break
        elif follow_choice in ("look", "l"):
            print("You look into the trees and carefully scan for whatever made the noise.")
            break
        else:
            print("Please type 'follow' or 'look' (or 'f'/'l').")
elif choice == second_option:
    print("You pick up the match and strike it, and for an instant, the forest around you is illuminated. You see a large grizzly bear, and then the match burns out. Do you want to RUN, or HIDE behind a tree?")
else:
    print("Make a choice")