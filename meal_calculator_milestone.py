# Meal Calculator

child_meal_price = float(input("What is the price of a child's meal? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
num_children = int(input("How many children are there? "))
num_adults = int(input("How many adults are there? "))

subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)
print()
print(f"Subtotal: ${subtotal:.2f}")