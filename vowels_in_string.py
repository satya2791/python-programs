# Program that prints the vowels in the string
# asks the users input
user_input = input("Enter a string: ")
# Define vowels both lower and upper case
vowels = "aeiouAEIOU"
# Use list comprehension to collect vowels in string
result = [char for char in user_input if char in vowels];
print(f"The vowels in the given string {user_input} is: ",result)