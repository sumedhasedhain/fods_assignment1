'''Function that accepts a string and calculate the number of upper case letters and lower case letters
'''

def count_case_letters(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return upper, lower

# Example usage
string = "Hello World! How are you?"
upper, lower = count_case_letters(string)
print(f"Uppercase: {upper}, Lowercase: {lower}")