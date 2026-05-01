# Simple Procedural Calculator

print("--- Calculator ---")
print("Options: +, -, *, /")

# Get user input
num1 = float(input("Enter first number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

# Perform calculation based on operator
if op == "+":
    result = num1 + num2
elif op == "-":
    result = num1 - num2
elif op == "*":
    result = num1 * num2
elif op == "/":
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Invalid Operator"

print(f"Result: {result}")
