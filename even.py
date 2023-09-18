#  A python script to find the sum of even numbers.

def sum_even_numbers(n):
    total = 0 
    
    # Start from 1 and iterate through numbers up to 'n'
    start_number = 1
    while start_number <= n:
        if start_number % 2 == 0:
            total += start_number
        start_number += 1
    
    return total

# Prompt the user to enter a positive integer 'n'
try:
    n = int(input("Enter a positive integer 'n': "))
    
    if n < 1:
        print("Please enter a positive integer.")
    else:
        # Calculate and display the sum of even numbers
        result = sum_even_numbers(n)
        print(f"The sum of even numbers from 1 to {n} is: {result}")
except ValueError:
    print(" Please enter a positive integer.")
