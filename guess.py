# Write a python code to generate a random number between 1 to 100

import random

number = random.randint(1, 100)

my_guess = int(input("Enter your guess : "))
guesses = 0
while True:
	guesses += 1
	if my_guess < number:
		print("too low")
	elif my_guess > number:
		print("too high")
	else:
		print("you won")
		break

if my_guess == number:
	print("congratultions")
else:
	print("game over")

