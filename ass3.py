import random

# Generate a random number between 1 and 20
random_number = random.randint(1, 20)

# Ask the user to enter their guess and check if the guess is correct
while True:
    user_guess = int(input("Guess the number between 1 and 20: "))
    if user_guess == random_number:
        print("Hurray! You won. The random number was", random_number)
        break
    elif user_guess < random_number:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")


