# Shpping Cart Program

print("Welcome to the Shopping Cart Program!\n")
cart = []

def print_menu():
    print("Please select one of the following:")
    print("1. Add item")
    print("2. View cart")
    print("3. Remove item")
    print("4. Compute total")
    print("5. Quit\n")

while True:
    print_menu()
    try:
        action = int(input("Please enter an action: "))
    except ValueError:
        print("Invalid input. Enter a number 1-5.\n")
        continue

    if action == 1:
        item = input("What item would you like to add? ")
        cart.append(item)
        print(f"'{item}' has been added to the cart.\n")
    elif action == 2:
        print("The contents of the shopping cart are:")
        if cart:
            for item in cart:
                print(item)
        else:
            print("Cart is empty.")
        print()
    elif action == 3:
        item = input("What item would you like to remove? ")
        if item in cart:
            cart.remove(item)
            print(f"'{item}' has been removed from the cart.\n")
        else:
            print(f"'{item}' is not in the cart.\n")
    elif action == 4:
        print("Total computation is not available as items do not have prices.\n")
    elif action == 5:
        print("Thank you. Goodbye.\n")
        break
    else:
        print("Invalid action. Please try again.\n")





