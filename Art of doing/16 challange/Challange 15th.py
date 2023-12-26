#Welcome to the Account Shipping Program
print("Welocme to the Account Shipping Program")
#define account name list
name_list=['Dinesh','Nishant','Ashish','Amrik','Bobby']
user_name=input("\nHello, What's your name:").title()
if user_name in name_list:
    print(f"Hello {user_name}. Welcome back to your account.")
    print("Current shipping price are as follows:")
    #summary of shipping prices
    print("\nShipping orders 0 to 100:\t\t\t\t$5.10 each")
    print("\nShipping orders 100 to 500:\t\t\t\t$5.00 each")
    print("\nShipping orders 500 to 1000:\t\t\t$4.95 each")
    print("\nShipping orders over 1000:\t\t\t\t$4.80 each")
    #get items form user
    order=int(input("\nHow many items would you like to ship:"))
    if order > 0 and order < 100:
        per_item=5.10
    elif order >100 and order <500:
        per_item=5.00
    elif order >500 and order <1000:
        per_item=4.95
    else:
        per_item=4.80
    #bill of orders
    print(f"To ship {order} items it will cost you ${round((order*per_item),2)} at ${per_item} per item.")
    #ask user to place the order
    place_order=input("Would you ot place this order (y/n):")
    if place_order == "y" or place_order == "Y":
        print(f"Okay. Shipping you {order} items.")
    else:
        print("Ok, Thank you, for exploring our services.")
#if user is not in user_list
else:
    print("Sorry, you do not have an account with us. Goodbye.")
