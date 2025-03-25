''' To calculate the Euclidean distance between two points based on user input
'''

import math

x1, y1 = map(float, input("Enter the first coordinate (x1, y1): ").split())
x2, y2 = map(float, input("Enter the second coordinate (x2, y2): ").split())

# Calculate the Euclidean distance
distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Display the result
print(f"The Euclidean distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.2f}")
