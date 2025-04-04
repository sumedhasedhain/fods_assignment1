'''
Set operations: Union, Intersection, Symmetric Difference, Adding, and Removing Elements.
'''

# Define the sets
set1 = {20, 40, 60}
set2 = {10, 20, 30, 40, 50, 60}

union_set = set1 | set2  # or set1.union(set2)
print("Union of set1 and set2:", union_set)
print("Length of the union set:", len(union_set))

intersection_set = set1 & set2  # or set1.intersection(set2)
print("Intersection of set1 and set2:", intersection_set)

sym_diff_set = set1 ^ set2  # or set1.symmetric_difference(set2)
print("Symmetric Difference of set1 and set2:", sym_diff_set)

set1.add(40)  # 40 is already present, so set remains the same
print("After adding 40 to set1:", set1)  # No change

set2.discard(20)  # Using discard to avoid KeyError if value is not found
print("After removing 20 from set2:", set2)