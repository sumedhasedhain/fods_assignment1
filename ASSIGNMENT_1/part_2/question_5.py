''' The formula for calculating simple interest is (principal * rate_of_interest * time_period) / 100
'''

principal = float(input("Enter the principal amount: "))
rate_of_interest = float(input("Enter the rate of interest (in %): "))
time_period = float(input("Enter the time period (in years): "))

# Calculate Simple Interest
simple_interest = (principal * rate_of_interest * time_period) / 100

# Display the result
print(f"The Simple Interest is: {simple_interest:.2f}")
