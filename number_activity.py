numbers = []

user_number = -1

while user_number != 0:
    # ask the user for a number
    user_number = int(input("Enter a number (0 to stop): "))

    # check for zero
    if user_number != 0:
      # put it into the list
      numbers.append(user_number)

sum = 0

for number in numbers:
    sum += number

count = len(numbers)
average = sum / count if count > 0 else 0

largest = numbers[0] if count > 0 else 0

for number in numbers:
    if number > largest:
        largest = number

# Check for the smallest positive number
smallest_positive = None

for number in numbers:
    if number > 0 and (smallest_positive is None or number < smallest_positive):
        smallest_positive = number

print(f"The sum is: {sum}")
print(f"The average is: {average}")
print(f"The largest number is: {largest}")
print(f"The smallest positive number is: {smallest_positive if smallest_positive is not None else 'None'}")