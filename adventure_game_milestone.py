print("Welcome to the Adventure Game!")
print("You find yourself in a dark forest. There are paths to the north, east, south, and west.")
print("What do you want to do?")

choice = input("Enter a direction (NORTH, EAST, SOUTH, WEST): ").lower()

if choice == "north":
    print("You head north into the mountains.")
elif choice == "east":
    print("You walk east towards the river.")
elif choice == "south":
    print("You venture south into the jungle.")
elif choice == "west":
    print("You explore the western caves.")
else:
    print("Invalid direction. Please choose north, east, south, or west.")

