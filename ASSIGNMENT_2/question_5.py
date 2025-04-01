'''To run a program called calculator with functions to perform arithmetic calculations
'''
def addition(a, b):
 return a + b
def subtraction(a, b):
 return a - b
def multiplication(a, b):
 return a * b
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."
def truncated_division(a, b):
    if b != 0:
        return a // b
    else:
        return "Error! Division by zero."
def modulus(a, b):
    if b != 0:
        return a % b
    else:
        return "Error! Division by zero."
def exponentiation(a, b):
    return a ** b

def calculator():
    print("Welcome to the Calculator!")
    
    # Taking input from the user
    a = float(input("Enter the first decimal number: "))
    b = float(input("Enter the second decimal number: "))
    
    # Performing the operations
    print(f"{a} + {b} = {addition(a, b)} (Addition)")
    print(f"{a} - {b} = {subtraction(a, b)} (Subtraction)")
    print(f"{a} * {b} = {multiplication(a, b)} (Multiplication)")
    print(f"{a} / {b} = {division(a, b)} (Division)")
    print(f"{a} // {b} = {truncated_division(a, b)} (Truncated Division)")
    print(f"{a} % {b} = {modulus(a, b)} (Modulus)")
    print(f"{a} ** {b} = {exponentiation(a, b)} (Exponentiation)")

# Run the calculator
calculator()
