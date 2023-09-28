class Calculator:
	def __init__(solve, a, b):
		solve.a = a
		solve.b = b
		
	def sum(solve):
		return solve.a + solve.b
		
	def subtract(solve):
		return solve.a  - solve.b
		
	def multiply(solve):
		return solve.a * solve.b
		
	def divide(solve):
				if solve.b == 0:
					return "cannot be divided by zero"
				else:
						return solve.a / solve.b
		
	def modulo(solve):
		return solve.a % solve.b
		
	def __str__(solve):
		return f"{solve.a}  {solve.b}"

num1, num2 = map(int, (input("Welcome, please enter only postive integer values for num1, num2 separated by comma: ").split(", ")))


pa = Calculator(30, 5)
print(pa.sum())
print(pa.subtract())
print(pa.multiply())
print(pa.divide())
print(pa.modulo())
