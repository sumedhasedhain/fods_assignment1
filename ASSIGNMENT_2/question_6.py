''' Program that asks the user to enter a list of names, stores them in a list, and count how many times the letter 'a' appears in the entire list
'''

# Function to count occurrences of 'a' in the list of names
def count_a(names_list):
    count = 0
    for name in names_list:
        count += name.lower().count('a')  
    return count

names = [] 
print("Enter the names one by one and when done, just hit enter without typing anything else.")

while True:
    name = input("Enter a name: ").strip() 
    if name == "":
        break  
    names.append(name) 

# Count how many times 'a' appears in the list of names
a_count = count_a(names)

# Display the result
print(f"The letter 'a' appears {a_count} times in the list of names.")
