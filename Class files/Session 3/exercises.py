# Q1 Continuously ask the user to enter a number until they provide a blank input. Output the sum of all the numbers.

# sum = 0
# number = 0
# while number != "":
#     number = input("Enter a number")
#     if number != "":
#         sum += int(number)
# print(f"Your numbers sum to {sum}")

# Q2. Ask the user to enter an integer number. Print all the odd numbers between 0 and that number (inclusive). 
# (Its ok not to worry about negative numbers for now, unlessyou really want a challenge.)

# print("The first number is 0")
# large_number = int(input("Enter a number"))
# while (large_number > 0):
#     if(large_number % 2 != 0):
#         print (large_number)
#     large_number = large_number -1


# Q3. Write a guessing game. Select a number and save it in your code. Ask your user for a number and get them to keep guessing until they get it.

# print("Guess the random number ")
# number = 76
# guess_attempt = int(input("Make a guess "))

# while(guess_attempt != number):
#     if guess_attempt < number:
#         print("Too low...")        
#     else:
#         print("Too high...")
#         guess_attempt = int(input("Make another attempt"))
# print("Correct!")


# FOR LOOPS

# Q1
# Ask the user for a number. Use a for loop to print the times table for that number up to ten.

# numbers = [1,11]
# to_multiply = int(input("Give me a number"))
# for number in range(1,11):
#     print(f"{to_multiply} x {number} = {to_multiply*number}")

# Q2
# Ask the user for an integer. Using a for loop, add up every number from 0 up to that integer and print the result

# max_number = int(input("Please enter a number"))
# total = 0

# for number in range(0, max_number+1):
#     total += number
# print(total)

# Another way of doing Q2:

# user_number = int(input("Enter a number"))
# list_of_numbers = []

# for number in range(0,user_number+1):
#     list_of_numbers.append(number)
#     total = sum(list_of_numbers)
# print(total)




