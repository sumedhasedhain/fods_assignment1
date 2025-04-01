'''Function to check whether the given number is Armstrong or not
'''
def is_armstrong(n):
    digits = str(n)
    
    num_digits = len(digits)
    
    # Calculate the sum of each digit raised to the power of the number of digits
    sum_of_powers = sum(int(digit) ** num_digits for digit in digits)
    
    # Check if the sum is equal to the original number
    if sum_of_powers == n:
        return True
    else:
        return False

# Test the function
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")
