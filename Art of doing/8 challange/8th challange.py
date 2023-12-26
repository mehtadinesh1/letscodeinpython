#Grocery List App
import datetime
print("Welcome to the Grocery List App.")
#print date and time by importing datetime library
today=datetime.datetime.today()
date_time = today.strftime("%m/%d \t %H:%M")
print("Current Date and Time:",date_time)

#creat list with two item inside it
c_list = ['Meat','Cheese']
print(f"You currently have {c_list[0]} and {c_list[1]} in your list")

#let the user add three item in list
item_1= input("\nType of food to add to the grocery list:\t").title()
item_2 = input("Type of food to add to the grocery list:\t").title()
item_3=input("Type of food to add to the grocery list:\t").title()
c_list.extend([item_1,item_2,item_3])

#display the list after the user add the items
print("\nHere is your grocery list:")
print(c_list)
print("Here is your grocery list sorted:")
c_list.sort()
print(c_list)

#simulating process
print("\nSimulating grocery shopping.....")

print(f"\nCurrent grocery list: {len(c_list)} items")
print(c_list)
item_buy = input("what food did you just buy:\t").title()
c_list.remove(item_buy)
print(f"Removing {item_buy} from list...")

print(f"\nCurrent grocery list: {len(c_list)} items")
print(c_list)
item_buy =input("What food did you just buy:\t").title()
c_list.remove(item_buy)
print(f"Removing {item_buy} from list...")

print(f"\nCurrent grocery list: {len(c_list)} items")
print(c_list)
item_buy = input("What food did you just buy:\t").title()
c_list.remove(item_buy)
print(f"Removing {item_buy} from list...")

print(f"\nCurrent grocery list: {len(c_list)} items")
print(c_list)
c_list.remove('Meat')

print("\nSorry, the store is out of Meat.")
add_item = input("What food would you like instead:\t")
c_list.append(add_item)
print("\nHere is what remains on your grocery list:")
print(c_list)

'''learning things
example
user=input("anything youwant").use_built_funtions'''