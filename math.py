# Accept input of two numbers and store in variables

num1, num2 = input("Enter two numbers: ").split()

num1 = int(num1)
num2 = int(num2)

# Add the two numbers and store in a variable called sum

sum = num1 + num2

# Print out result
print("{} + {} = {}".format(num1, num2, sum))

