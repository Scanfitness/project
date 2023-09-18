# Factorial calculation

def calculate_factorial(n):
    factorial = 1
    while n > 0:
        factorial *= n
        n -= 1
    
    return factorial

# Prompt the user to enter a positive integer 'n'
try:
    n = int(input("Enter a positive integer 'n': "))
    
    if n < 0:
        print("Please enter a positive integer.")
    else:
        # Calculate and display the factorial
        result = calculate_factorial(n)
        print(f"The factorial of {n} is: {result}")
except ValueError:
    print("Please enter a positive integer.")

