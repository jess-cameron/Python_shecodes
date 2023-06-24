# Q1. The dictionary below represents the cost of individual items in a supermarket. 
# Write a program that asks the user how many of each item they would like in turn, and outputs the total cost of their groceries.

grocery_list = []
total = sum(grocery_list)
groceries = {"Baby Spinach": 2.78,"Hot Chocolate": 3.70,"Crackers": 2.10,"Coffee": 9.00,"Carrots": 0.56,"Oranges": 3.08}
for key in groceries.keys():
    print (key)
    grocery_list = int(input("how many? "))
for value in groceries.values():
    grocery_list.append(value)
print(total)









# user_number = int(input("Enter a number"))
# list_of_numbers = []

# for number in range(0,user_number+1):
#     list_of_numbers.append(number)
#     total = sum(list_of_numbers)
# print(total)