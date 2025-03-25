''' Program that accepts a string and calculates the number of digits and letters 
'''

input_string = input("Enter a string: ")

digit_count = 0
letter_count = 0

# Loop through each character in the string
for char in input_string:
    if char.isdigit():  
        digit_count += 1
    else:
        if char.isalpha():  
         letter_count += 1

# Display the result
print(f"Number of digits: {digit_count}")
print(f"Number of letters: {letter_count}")
