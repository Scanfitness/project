# Write a program that will assign a random signed number to the variable number each time it is executed.

import random

# Generate a random signed number between -10 and 10
number = random.randint(-10, 10)

#Print the number
print(number, end= " ")

# Check if the number is zero, negative or positive
if number > 0:
    print("is positive")
elif number == 0:
    print("is zero")
else:
    print("is negative")

print()

