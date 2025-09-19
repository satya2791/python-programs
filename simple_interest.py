# Program to calculate simple interest
# Formula: SI = (P * R * T) / 100
# Where P = Principal amount, R = Rate of interest, T = Time period in years
# SI = Simple Interest
# Ask the user to input the values for P, R, and T
User_input1 = int(input("Enter the principal amount: "))
User_input2 = int(input("Enter the rate of interest: "))
User_input3 = int(input("The time period in years: "))
# Calculate simple interest
SI = (User_input1 * User_input2 * User_input3) / 100
# Print the result
print("The simple interest is: ", SI)
