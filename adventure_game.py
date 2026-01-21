# Adventure Game
# Expanded Version with Sub-Options

print("Welcome to the Adventure Game!")
print("You find yourself in a dark forest. There are paths to the north, east, south, and west.")
print("What do you want to do?")

choice = input("Enter a direction (NORTH, EAST, SOUTH, WEST): ").lower()

if choice == "north":
    print("You head north into the mountains.")
    
    option = input("Choose an option (CLIMB, EXPLORE, RETURN): ").lower()
    if option == "climb":
        print("You climb the mountain and enjoy the view.")
        sub_option = input("Choose a sub-option (ENJOY, DESCEND): ").lower()
        if sub_option == "enjoy":
            print("You take a moment to appreciate the beauty around you.")
        elif sub_option == "descend":
            print("You carefully descend the mountain.")
        else:
            print("Please type 'ENJOY' or 'DESCEND'.")
    elif option == "explore":
        print("You explore the mountain and find a hidden cave.")
        sub_option = input("Choose a sub-option (ENTER, LEAVE): ").lower()
        if sub_option == "enter":
            print("You enter the cave and discover ancient paintings.")
        elif sub_option == "leave":
            print("You leave the cave and return to the mountain path.")
        else:
            print("Please type 'ENTER' or 'LEAVE'.")
    elif option == "return":
        sub_option = input("Choose a sub-option (FOREST, MOUNTAIN): ").lower()
        if sub_option == "forest":
            print("You return to the forest.")
        elif sub_option == "mountain":
            print("You head back up the mountain.")
        else:
            print("Please type 'FOREST' or 'MOUNTAIN'.")
    else:
        print("Please type 'CLIMB', 'EXPLORE', or 'RETURN'.")
elif choice == "east":
    print("You walk east towards the river.")
    option = input("Choose an option (SWIM, FISH, RETURN): ").lower()
    if option == "swim":
        print("You swim in the river and feel refreshed.")
        sub_option = input("Choose a sub-option (FLOAT, DIVE): ").lower()
        if sub_option == "float":
            print("You float peacefully down the river.")
        elif sub_option == "dive":
            print("You dive into the river and explore underwater.")
        else:
            print("Please type 'FLOAT' or 'DIVE'.")
    elif option == "fish":
        print("You catch a fish and prepare a meal.")
        sub_option = input("Choose a sub-option (COOK, RELEASE): ").lower()
        if sub_option == "cook":
            print("You cook the fish over a campfire.")
        elif sub_option == "release":
            print("You release the fish back into the river.")
        else:
            print("Please type 'COOK' or 'RELEASE'.")
    elif option == "return":
        print("You return to the forest.")
        sub_option = input("Choose a sub-option (NORTH, EAST): ").lower()
        if sub_option == "north":
            print("You head north into the mountains.")
        elif sub_option == "east":
            print("You walk east towards the river.")
        else:
            print("Please type 'NORTH' or 'EAST'.")
    else:
        print("Please type 'SWIM', 'FISH', or 'RETURN'.")
elif choice == "south":
    print("You venture south into the jungle.")
    option = input("Choose an option (HUNT, EXPLORE, RETURN): ").lower()
    if option == "hunt":
        print("You hunt for food and gather supplies.")
        sub_option = input("Choose a sub-option (COOK, STORE): ").lower()
        if sub_option == "cook":
            print("You cook your food over a fire.")
        elif sub_option == "store":
            print("You store your supplies for later.")
        else:
            print("Please type 'COOK' or 'STORE'.")
    elif option == "explore":
        print("You explore the jungle and find exotic plants.")
        sub_option = input("Choose a sub-option (COLLECT, LEAVE): ").lower()
        if sub_option == "collect":
            print("You collect samples of the exotic plants.")
        elif sub_option == "leave":
            print("You leave the plants undisturbed.")
        else:
            print("Please type 'COLLECT' or 'LEAVE'.")
    elif option == "return":
        print("You return to the forest.")
        sub_option = input("Choose a sub-option (NORTH, SOUTH): ").lower()
        if sub_option == "north":
            print("You head north into the mountains.")
        elif sub_option == "south":
            print("You venture south into the jungle.")
        else:
            print("Please type 'NORTH' or 'SOUTH'.")
    else:
        print("Please type 'HUNT', 'EXPLORE', or 'RETURN'.")
elif choice == "west":
    print("You explore the western caves.")
    option = input("Choose an option (EXPLORE, MINE, RETURN): ").lower()
    if option == "explore":
        print("You explore the caves and find sparkling gems.")
        sub_option = input("Choose a sub-option (COLLECT, LEAVE): ").lower()
        if sub_option == "collect":
            print("You collect some of the sparkling gems.")
        elif sub_option == "leave":
            print("You leave the gems untouched.")
        else:
            print("Please type 'COLLECT' or 'LEAVE'.")
    elif option == "mine":
        print("You mine for resources and gather valuable minerals.")
        sub_option = input("Choose a sub-option (STORE, TRADE): ").lower()
        if sub_option == "store":
            print("You store the minerals in your backpack.")
        elif sub_option == "trade":
            print("You trade the minerals with a passing merchant.")
        else:
            print("Please type 'STORE' or 'TRADE'.")
    elif option == "return":
        print("You return to the forest.")
        sub_option = input("Choose a sub-option (NORTH, WEST): ").lower()
        if sub_option == "north":
            print("You head north into the mountains.")
        elif sub_option == "west":
            print("You explore the western caves.")
        else:
            print("Please type 'NORTH' or 'WEST'.")
    else:
        print("Please type 'EXPLORE', 'MINE', or 'RETURN'.")
else:
    print("Invalid direction. Please choose north, east, south, or west.")

