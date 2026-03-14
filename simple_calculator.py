# Simple Python Calculator
# Created while learning Python basics

# Ask user for numbers
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

# Perform calculations
addition = first_number + second_number
subtraction = first_number - second_number
multiplication = first_number * second_number
division = first6_number / second_number if second_number != 0 else "undefined (division by zero)"

# Show results
print("\n--- Calculation Results ---")
print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")