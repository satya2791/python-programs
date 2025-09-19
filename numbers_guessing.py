# Program that guess the number in the range of 1 to 100 
# provides whether the guess number is too low or too high or correct 

# import random modules 
import random
# storing a random number from 1 to 100 in random_number variable
random_number = random.randint(1,100)
# loop will continue until the guess number is correct
while True:
  # ask user for input
  user_input = int(input("Guess an integer from 1 to 100: "))
  # print too if low user_input is less than random_number 
  if user_input < random_number:
     print("Guess is too low")
  # print too high if user_input is greater than random_number 
  elif user_input > random_number:
     print("Guess is too high")
  # print guess is correct if user_input is equal to random_number 
  elif user_input == random_number:
     print("Your guess is correct")
     # break the loop when guess is correct 
     break
  else:
     print("Oops error,please enter a number ranges from 1 to 100")