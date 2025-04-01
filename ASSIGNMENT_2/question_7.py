''' Program that requires users to enter integer values to populate lists then print messages
'''
def get_integer_list(prompt):
    integer_list = []
    print(prompt)
    while True:
        try:
            num = input("Enter an integer (or type 'done' to finish): ").strip()
            if num.lower() == 'done':
                break
            integer_list.append(int(num))
        except ValueError:
            print("Please enter a valid integer or 'done' to finish.")
    return integer_list

list1 = get_integer_list("Enter integers for the first list:")
list2 = get_integer_list("Enter integers for the second list:")

if len(list1) == len(list2):
    print("The lists are of the same length.")
else:
    print("The lists are not of the same length.")


if sum(list1) == sum(list2):
    print("The sum of elements in both lists is the same.")
else:
    print("The sum of elements in both lists is different.")

common_values = set(list1) & set(list2)  
if common_values:
    print(f"The following values occur in both lists: {common_values}")
else:
    print("There are no common values between the lists.")
