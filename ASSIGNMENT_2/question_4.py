''' Function to accept a list of names and return the sorted order of names back.
'''

def sort_names(names):
    # Sort the list of names in alphabetical order
    return sorted(names)

# Test the function
names_list = input("Enter a list of names separated by commas: ").split(',')
# Strip any leading/trailing spaces from each name
names_list = [name.strip() for name in names_list]

sorted_names = sort_names(names_list)
print("Sorted names:", sorted_names)
