# Shopping Cart Program
# This program allows users to manage a shopping cart with persistent storage.

import json
import os

CART_FILE = os.path.join(os.path.dirname(__file__), "cart.json")

def load_cart():
    if os.path.exists(CART_FILE):
        try:
            with open(CART_FILE, "r", encoding="utf-8") as f:
                data = json.load(f)
                if isinstance(data, list):
                    return [list(entry) for entry in data]
        except Exception:
            pass
    return []

def save_cart(cart):
    try:
        with open(CART_FILE, "w", encoding="utf-8") as f:
            json.dump(cart, f, indent=2)
    except Exception as e:
        print(f"Warning: failed to save cart: {e}")

print("Welcome to the Shopping Cart Program!\n")
cart = load_cart()

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
        price = float(input(f"What is the price of '{item}'? "))
        cart.append([item, price])
        save_cart(cart)
        print(f"'{item}' has been added to the cart.\n")
    elif action == 2:
        print("The contents of the shopping cart are:")
        if cart:
            for i, (item, price) in enumerate(cart, start=1):
                print(f"{i}. {item} - ${price:.2f}")
        else:
            print("Cart is empty.")
        print()
    elif action == 3:
        print("The contents of the shopping cart are:")
        if cart:
            for i, (item, price) in enumerate(cart, start=1):
                print(f"{i}. {item} - ${price:.2f}")
        item = input("Which item would you like to remove? ")
        try:
            item_index = int(item) - 1
            if 0 <= item_index < len(cart):
                removed_item = cart.pop(item_index)
                save_cart(cart)
                print(f"'{removed_item[0]}' has been removed from the cart.\n")
            else:
                print(f"Item number {item} is not in the cart.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")
    elif action == 4:
        total = sum(price for item, price in cart)
        print(f"The total price of the items in the shopping cart is ${total:.2f}\n")
    elif action == 5:
        save_cart(cart)
        print("Thank you. Goodbye.\n")
        break
    else:
        print("Invalid action. Please try again.\n")





