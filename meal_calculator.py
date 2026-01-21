# Meal Calculator
# This program calculates the total cost of a meal including
# additional costs, sales tax, tip, and change based on user input.

print("Welcome to the Meal Calculator!")
print()
additional_costs = input("Are there any additional costs (drinks, desserts, etc.)? (yes/no) ")
number_of_additional_items = 0
additional_cost_per_item = 0.0

if additional_costs.lower() == 'yes':
    number_of_additional_items = int(input("How many additional items are there? "))

    additional_item_names = []
    for i in range(number_of_additional_items):
        item_name = input(f"What is the name of additional item {i+1}? ").lower()
        additional_item_names.append(item_name)
    print()    

    child_meal_price = float(input("What is the price of a child's meal? "))
    child_additional_cost_per_item = []
    for i in range(number_of_additional_items):
        child_additional_cost_per_item.append(float(input(f"What is the price of child's {additional_item_names[i]}? ")))

    adult_meal_price = float(input("What is the price of an adult's meal? "))
    adult_additional_cost_per_item = []
    for i in range(number_of_additional_items):
        adult_additional_cost_per_item.append(float(input(f"What is the price of adult's {additional_item_names[i]}? ")))

    num_children = int(input("How many children are there? "))
    num_adults = int(input("How many adults are there? "))

    subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)
    for i in range(number_of_additional_items):
        subtotal += (child_additional_cost_per_item[i] * num_children) + (adult_additional_cost_per_item[i] * num_adults)
    print()
    print(f"Subtotal: ${subtotal:.2f}")
else:
    child_meal_price = float(input("What is the price of a child's meal? "))
    adult_meal_price = float(input("What is the price of an adult's meal? "))
    num_children = int(input("How many children are there? "))
    num_adults = int(input("How many adults are there? "))

    subtotal = (child_meal_price * num_children) + (adult_meal_price * num_adults)
    print()
    print(f"Subtotal: ${subtotal:.2f}")

sales_tax_rate = float(input("What is the sales tax rate? "))
sales_tax = subtotal * (sales_tax_rate / 100)
print()
print(f"Sales Tax: ${sales_tax:.2f}")

total = subtotal + sales_tax
print()
print(f"Total: ${total:.2f}")

tip_rate = float(input("What is the tip rate? "))
tip = total * (tip_rate / 100)
print()
print(f"Tip: ${tip:.2f}")

payment_amount = float(input("What is the payment amount? "))
change = payment_amount - (total + tip)
print()
print(f"Change: ${change:.2f}")
